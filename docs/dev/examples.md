# Usage Examples

## User Management

### User Registration and Approval
```python
# views.py
class RegisterView(CreateView):
    template_name = 'netdash/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('netdash:pending_approval')

@user_passes_test(lambda u: u.is_staff)
def approve_user(request, user_id):
    try:
        user = User.objects.get(id=user_id, is_approved=False)
        user.is_approved = True
        user.approval_date = timezone.now()
        user.save()
        messages.success(request, f'User {user.username} has been approved.')
    except User.DoesNotExist:
        messages.error(request, 'User not found or already approved.')
    return redirect('netdash:user_approval_list')
```

### Template Usage
```html
{% extends "base/base.html" %}

{% block content %}
<div class="card">
    <div class="card-header">
        <h5 class="card-title mb-0">Register New Account</h5>
    </div>
    <div class="card-body">
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit" class="btn btn-primary">Register</button>
        </form>
    </div>
</div>
{% endblock %}
```

## Device Management

### Adding a New Device
```python
# models.py
class NetworkDevice(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ip_address = models.GenericIPAddressField()
    device_type = models.CharField(max_length=50, choices=DEVICE_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    last_seen = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.ip_address})"

# views.py
class DeviceCreateView(LoginRequiredMixin, CreateView):
    model = NetworkDevice
    form_class = NetworkDeviceForm
    template_name = 'netdevices/device_form.html'
    success_url = reverse_lazy('netdevices:device_list')

    def form_valid(self, form):
        messages.success(self.request, 'Device added successfully.')
        return super().form_valid(form)
```

### Configuration Management
```python
# Example configuration template
device_config = {
    'hostname': device.name,
    'interfaces': [
        {
            'name': 'GigabitEthernet0/1',
            'ip_address': '192.168.1.1',
            'subnet_mask': '255.255.255.0',
            'enabled': True
        }
    ],
    'routing': {
        'ospf': {
            'process_id': 1,
            'networks': ['192.168.1.0/24']
        }
    }
}

# Deployment function
def deploy_config(device, config):
    try:
        with device.connect() as conn:
            conn.send_config_set(config.to_commands())
            conn.save_config()
        return True, "Configuration deployed successfully"
    except Exception as e:
        return False, f"Deployment failed: {str(e)}"
```

## Error Handling

### Form Validation
```python
class DeviceForm(forms.ModelForm):
    class Meta:
        model = NetworkDevice
        fields = ['name', 'ip_address', 'device_type']

    def clean_ip_address(self):
        ip = self.cleaned_data['ip_address']
        if NetworkDevice.objects.filter(ip_address=ip).exists():
            raise ValidationError('This IP address is already in use.')
        return ip

    def clean(self):
        cleaned_data = super().clean()
        device_type = cleaned_data.get('device_type')
        name = cleaned_data.get('name')
        
        if device_type and name:
            if not name.startswith(device_type.prefix):
                raise ValidationError(
                    f"Device name must start with {device_type.prefix}"
                )
```

### API Error Handling
```python
from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if response is not None:
        response.data['status_code'] = response.status_code
        response.data['detail'] = str(exc)
        
        if hasattr(exc, 'get_full_details'):
            response.data['errors'] = exc.get_full_details()
    
    return response
```

## Authentication Middleware

### Approval Check
```python
class UserApprovalMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if not request.user.is_approved:
                if not any(url in request.path 
                          for url in settings.APPROVAL_EXEMPT_URLS):
                    return redirect('netdash:pending_approval')
        return self.get_response(request)
```

## Template Tags

### Custom Filters
```python
from django import template

register = template.Library()

@register.filter
def device_status_class(status):
    return {
        'online': 'success',
        'offline': 'danger',
        'maintenance': 'warning'
    }.get(status, 'secondary')

@register.simple_tag
def get_device_count(status=None):
    if status:
        return NetworkDevice.objects.filter(status=status).count()
    return NetworkDevice.objects.count()
```

## HTMX Integration

### Dynamic Updates
```html
<!-- Device list with live updates -->
<div hx-get="{% url 'netdevices:device_list' %}"
     hx-trigger="every 30s"
     hx-swap="innerHTML">
    {% include 'netdevices/device_table.html' %}
</div>

<!-- Search with auto-complete -->
<input type="search" 
       name="q" 
       hx-get="{% url 'netdevices:search' %}"
       hx-trigger="keyup changed delay:500ms"
       hx-target="#search-results">
<div id="search-results"></div>
```

## Testing Examples

### Model Tests
```python
class NetworkDeviceTests(TestCase):
    def setUp(self):
        self.device = NetworkDevice.objects.create(
            name='test-router-01',
            ip_address='192.168.1.1',
            device_type='router'
        )

    def test_device_str(self):
        self.assertEqual(
            str(self.device),
            'test-router-01 (192.168.1.1)'
        )

    def test_device_status_update(self):
        self.device.update_status('maintenance')
        self.assertEqual(self.device.status, 'maintenance')
```

### View Tests
```python
class DeviceViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(
            username='testuser',
            password='testpass123'
        )

    def test_device_list_view(self):
        response = self.client.get(
            reverse('netdevices:device_list')
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'netdevices/device_list.html'
        )
```

## Command Examples

### Custom Management Commands
```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Sync device configurations'

    def add_arguments(self, parser):
        parser.add_argument(
            '--device',
            help='Sync specific device'
        )

    def handle(self, *args, **options):
        if options['device']:
            devices = NetworkDevice.objects.filter(
                name=options['device']
            )
        else:
            devices = NetworkDevice.objects.all()

        for device in devices:
            try:
                device.sync_config()
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully synced {device.name}'
                    )
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f'Failed to sync {device.name}: {str(e)}'
                    )
                )
