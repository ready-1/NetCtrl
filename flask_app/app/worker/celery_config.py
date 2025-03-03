import os
from celery import Celery
from celery.schedules import crontab

# Initialize Celery
celery = Celery(
    'netctrl',
    broker=os.environ.get('REDIS_URL', 'redis://localhost:6379/0'),
    backend=os.environ.get('REDIS_URL', 'redis://localhost:6379/0'),
    include=['app.worker.tasks']
)

# Configure Celery
celery.conf.update(
    # Task settings
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    enable_utc=True,
    
    # Concurrency settings
    worker_concurrency=5,  # Number of worker processes
    task_acks_late=True,   # Tasks are acknowledged after execution
    task_reject_on_worker_lost=True,  # Reject tasks if worker is lost
    
    # Task execution settings
    task_time_limit=600,      # Maximum runtime for a task (10 minutes)
    task_soft_time_limit=300, # Soft time limit (5 minutes) - sends exception
    
    # Rate limiting
    task_default_rate_limit='100/m',  # Default rate limit
    
    # Retry settings
    task_default_retry_delay=60,  # Default retry delay in seconds
    task_max_retries=3,           # Maximum number of retries
    
    # Beat schedule for periodic tasks
    beat_schedule={
        'poll-switches-config': {
            'task': 'app.worker.tasks.poll_switches_config',
            'schedule': crontab(minute='*/5'),  # Every 5 minutes
        },
        'poll-switches-metrics': {
            'task': 'app.worker.tasks.poll_switches_metrics',
            'schedule': crontab(minute='*/1'),  # Every minute
        },
    }
)

# Automatically discover tasks
celery.autodiscover_tasks(['app.worker'])

# Optional: Configure task routes
celery.conf.task_routes = {
    'app.worker.tasks.poll_switches_config': {'queue': 'config'},
    'app.worker.tasks.poll_switches_metrics': {'queue': 'metrics'},
    'app.worker.tasks.*': {'queue': 'default'},
}

# Start Celery in application context
def start_celery(app):
    """Start Celery with Flask application context."""
    class FlaskTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    
    celery.Task = FlaskTask
    return celery
