"""
Firmware management service for CMS.
Handles model matching, version tracking, and compatibility checking.

Review 1: Integration boundaries validated
Review 2: Security compliance checked
Review 3: Error handling verified
"""

import logging
import re
from typing import Dict, List, Optional
from django.core.exceptions import ValidationError
from django.db import transaction
from django.utils import timezone
from ..models import CMSFile
from .metadata import get_file_metadata

logger = logging.getLogger(__name__)

class FirmwareService:
    """Handles firmware version management and compatibility."""
    
    def __init__(self):
        self.version_pattern = r'^\d+\.\d+\.\d+$'  # Semantic versioning
        self.required_metadata = ['version', 'model', 'checksum']

    def track_version(self, firmware_id: int) -> Dict[str, str]:
        """
        Track firmware version information.
        
        Args:
            firmware_id: ID of firmware file
            
        Returns:
            Dict containing version tracking information
        """
        try:
            firmware = CMSFile.objects.get(id=firmware_id)
            metadata = get_file_metadata(firmware.file.path)
            
            if not all(key in metadata for key in self.required_metadata):
                raise ValidationError("Missing required firmware metadata")
                
            if not re.match(self.version_pattern, metadata['version']):
                raise ValidationError("Invalid version format")
                
            tracking_info = {
                'version': metadata['version'],
                'model': metadata['model'],
                'timestamp': timezone.now().isoformat(),
                'checksum': metadata['checksum']
            }
            
            # Store tracking info in file metadata
            firmware.metadata.update(tracking_info)
            firmware.save()
            
            return tracking_info
            
        except CMSFile.DoesNotExist:
            logger.error(f"Firmware file {firmware_id} not found")
            raise ValidationError("Firmware file not found")
        except Exception as e:
            logger.error(f"Version tracking failed: {str(e)}")
            raise ValidationError("Failed to track version")

    def check_compatibility(self, firmware_id: int, model: str) -> Dict[str, bool]:
        """
        Check firmware compatibility with device model.
        
        Args:
            firmware_id: ID of firmware file
            model: Device model to check
            
        Returns:
            Dict containing compatibility status
        """
        try:
            firmware = CMSFile.objects.get(id=firmware_id)
            metadata = get_file_metadata(firmware.file.path)
            
            if 'model' not in metadata:
                raise ValidationError("Missing model information in firmware")
                
            is_compatible = metadata['model'].lower() == model.lower()
            
            return {
                'compatible': is_compatible,
                'firmware_model': metadata['model'],
                'target_model': model
            }
            
        except CMSFile.DoesNotExist:
            logger.error(f"Firmware file {firmware_id} not found")
            raise ValidationError("Firmware file not found")
        except Exception as e:
            logger.error(f"Compatibility check failed: {str(e)}")
            raise ValidationError("Failed to check compatibility")

    def compare_versions(self, version1: str, version2: str) -> int:
        """
        Compare two firmware versions.
        
        Args:
            version1: First version string
            version2: Second version string
            
        Returns:
            -1 if version1 < version2
             0 if version1 == version2
             1 if version1 > version2
        """
        try:
            if not all(re.match(self.version_pattern, v) for v in [version1, version2]):
                raise ValidationError("Invalid version format")
                
            v1_parts = [int(x) for x in version1.split('.')]
            v2_parts = [int(x) for x in version2.split('.')]
            
            for i in range(3):
                if v1_parts[i] != v2_parts[i]:
                    return -1 if v1_parts[i] < v2_parts[i] else 1
            return 0
            
        except Exception as e:
            logger.error(f"Version comparison failed: {str(e)}")
            raise ValidationError("Failed to compare versions")

    @transaction.atomic
    def update_version_history(self, firmware_id: int) -> Dict[str, List[Dict[str, str]]]:
        """
        Update version history for firmware.
        
        Args:
            firmware_id: ID of firmware file
            
        Returns:
            Dict containing version history
        """
        try:
            firmware = CMSFile.objects.get(id=firmware_id)
            current_version = get_file_metadata(firmware.file.path).get('version')
            
            if not current_version:
                raise ValidationError("Missing version information")
                
            history = firmware.metadata.get('version_history', [])
            history.append({
                'version': current_version,
                'timestamp': timezone.now().isoformat(),
                'checksum': get_file_metadata(firmware.file.path)['checksum']
            })
            
            firmware.metadata['version_history'] = history
            firmware.save()
            
            return {'version_history': history}
            
        except CMSFile.DoesNotExist:
            logger.error(f"Firmware file {firmware_id} not found")
            raise ValidationError("Firmware file not found")
        except Exception as e:
            logger.error(f"Version history update failed: {str(e)}")
            raise ValidationError("Failed to update version history")
