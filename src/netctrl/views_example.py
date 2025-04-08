"""
Example Django views demonstrating the usage of the logging configuration
"""

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from netctrl.logging_config import get_logger

# Create a logger for this module with the 'django' service tag
logger = get_logger(__name__, 'django')

@require_http_methods(["GET"])
def api_status(request):
    """
    API endpoint to check the status of the application
    
    This example demonstrates different log levels and how they appear in the logs
    """
    logger.debug("Debug message: Detailed information for debugging")
    logger.info("Processing status request")
    
    try:
        # Simulate some application logic
        result = {
            "status": "ok",
            "version": "1.0.0",
            "environment": "development"
        }
        
        logger.info(f"Status request processed successfully: {result['status']}")
        return JsonResponse(result)
    
    except Exception as e:
        # Log errors with traceback
        logger.error(f"Error processing status request: {str(e)}", exc_info=True)
        
        # Demonstrate warning level
        logger.warning("This is a warning message that something might be wrong")
        
        # Return error response
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

@require_http_methods(["POST"])
def handle_upload(request):
    """
    API endpoint to handle file uploads
    
    Demonstrates structured logging with context information
    """
    logger.info("File upload request received")
    
    # Extract information from request
    file_name = request.FILES.get('file', None)
    if not file_name:
        logger.warning("No file provided in upload request")
        return JsonResponse({"status": "error", "message": "No file provided"}, status=400)
    
    # Log structured information
    logger.info(
        f"Processing file upload: {file_name}",
        extra={
            "file_name": str(file_name),
            "file_size": request.FILES['file'].size,
            "content_type": request.FILES['file'].content_type,
            "user_id": request.user.id if request.user.is_authenticated else None
        }
    )
    
    try:
        # Simulate file processing
        logger.debug(f"Starting file processing for {file_name}")
        
        # Simulate successful upload
        logger.info(f"File {file_name} uploaded successfully")
        return JsonResponse({"status": "success", "file_name": str(file_name)})
        
    except Exception as e:
        logger.error(f"Error processing file upload: {str(e)}", exc_info=True)
        return JsonResponse({"status": "error", "message": str(e)}, status=500)
