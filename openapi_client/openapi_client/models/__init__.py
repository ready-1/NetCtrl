# coding: utf-8

# flake8: noqa
"""
M4300 REST API

M4300 REST API with ConfigAgent Documentation.

The version of the OpenAPI document: 2.0.0.59
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from openapi_client.models.active_image_get import ActiveImageGet
from openapi_client.models.active_image_get200_response import ActiveImageGet200Response
from openapi_client.models.active_image_post import ActiveImagePost
from openapi_client.models.active_image_post_request import ActiveImagePostRequest
from openapi_client.models.auto_voip_cfg_get import AutoVoipCfgGet
from openapi_client.models.auto_voip_cfg_get_oui_based import AutoVoipCfgGetOuiBased
from openapi_client.models.auto_voip_cfg_get_protocol_based import (
    AutoVoipCfgGetProtocolBased,
)
from openapi_client.models.auto_voip_cfg_post import AutoVoipCfgPost
from openapi_client.models.auto_voip_cfg_post_oui_based import AutoVoipCfgPostOuiBased
from openapi_client.models.auto_voip_cfg_post_protocol_based import (
    AutoVoipCfgPostProtocolBased,
)
from openapi_client.models.bonjour import Bonjour
from openapi_client.models.bonjour_get200_response import BonjourGet200Response
from openapi_client.models.config_file_compare import ConfigFileCompare
from openapi_client.models.config_file_compare_get200_response import (
    ConfigFileCompareGet200Response,
)
from openapi_client.models.cos_queue_config_get200_response import (
    CosQueueConfigGet200Response,
)
from openapi_client.models.cos_queue_config_inner import CosQueueConfigInner
from openapi_client.models.cos_queue_config_inner_id import CosQueueConfigInnerId
from openapi_client.models.cos_queue_config_inner_min_bw import CosQueueConfigInnerMinBw
from openapi_client.models.cos_queue_config_post_request import (
    CosQueueConfigPostRequest,
)
from openapi_client.models.costrust import Costrust
from openapi_client.models.costrust_get200_response import CostrustGet200Response
from openapi_client.models.costrust_post_request import CostrustPostRequest
from openapi_client.models.device_cable_test import DeviceCableTest
from openapi_client.models.device_cable_test_get200_response import (
    DeviceCableTestGet200Response,
)
from openapi_client.models.device_info import DeviceInfo
from openapi_client.models.device_info_get200_response import DeviceInfoGet200Response
from openapi_client.models.device_info_temperature_sensors_inner import (
    DeviceInfoTemperatureSensorsInner,
)
from openapi_client.models.device_log_reader import DeviceLogReader
from openapi_client.models.device_log_reader_get200_response import (
    DeviceLogReaderGet200Response,
)
from openapi_client.models.device_name import DeviceName
from openapi_client.models.device_name_get200_response import DeviceNameGet200Response
from openapi_client.models.device_name_post_request import DeviceNamePostRequest
from openapi_client.models.device_reboot import DeviceReboot
from openapi_client.models.device_reboot_post_request import DeviceRebootPostRequest
from openapi_client.models.dot1d_base_config import Dot1dBaseConfig
from openapi_client.models.dot1d_base_config_get200_response import (
    Dot1dBaseConfigGet200Response,
)
from openapi_client.models.dot1d_stp_config import Dot1dStpConfig
from openapi_client.models.dot1d_stp_config_get200_response import (
    Dot1dStpConfigGet200Response,
)
from openapi_client.models.dot1d_stp_entries_get200_response import (
    Dot1dStpEntriesGet200Response,
)
from openapi_client.models.dot1d_stp_entries_inner import Dot1dStpEntriesInner
from openapi_client.models.dot1d_tp_config_get import Dot1dTpConfigGet
from openapi_client.models.dot1d_tp_config_get200_response import (
    Dot1dTpConfigGet200Response,
)
from openapi_client.models.dot1d_tp_config_post import Dot1dTpConfigPost
from openapi_client.models.dot1d_tp_config_post_request import Dot1dTpConfigPostRequest
from openapi_client.models.dot1d_tp_port_entries_get200_response import (
    Dot1dTpPortEntriesGet200Response,
)
from openapi_client.models.dot1d_tp_port_entries_inner import Dot1dTpPortEntriesInner
from openapi_client.models.dot1p_queue_map_get200_response import (
    Dot1pQueueMapGet200Response,
)
from openapi_client.models.dot1p_queue_map_inner import Dot1pQueueMapInner
from openapi_client.models.dot1p_queue_map_post_request import Dot1pQueueMapPostRequest
from openapi_client.models.dot1q_sw_port_config_get import Dot1qSwPortConfigGet
from openapi_client.models.dot1q_sw_port_config_get200_response import (
    Dot1qSwPortConfigGet200Response,
)
from openapi_client.models.dot1q_sw_port_config_post import Dot1qSwPortConfigPost
from openapi_client.models.dot1q_sw_port_config_post_request import (
    Dot1qSwPortConfigPostRequest,
)
from openapi_client.models.dot1s_interfaces_get200_response import (
    Dot1sInterfacesGet200Response,
)
from openapi_client.models.dot1s_interfaces_get_inner import Dot1sInterfacesGetInner
from openapi_client.models.dot1s_interfaces_post import Dot1sInterfacesPost
from openapi_client.models.dot1s_interfaces_post_request import (
    Dot1sInterfacesPostRequest,
)
from openapi_client.models.download import Download
from openapi_client.models.download_status import DownloadStatus
from openapi_client.models.dual_image_status import DualImageStatus
from openapi_client.models.dual_image_status_get200_response import (
    DualImageStatusGet200Response,
)
from openapi_client.models.fdb_stats_get import FdbStatsGet
from openapi_client.models.fdb_stats_get200_response import FdbStatsGet200Response
from openapi_client.models.fdb_stats_post import FdbStatsPost
from openapi_client.models.fdb_stats_post_request import FdbStatsPostRequest
from openapi_client.models.fdbs_get200_response import FdbsGet200Response
from openapi_client.models.fdbs_inner import FdbsInner
from openapi_client.models.fiber_optics import FiberOptics
from openapi_client.models.fiber_optics_get200_response import FiberOpticsGet200Response
from openapi_client.models.general_responses_code import GeneralResponsesCode
from openapi_client.models.host_table import HostTable
from openapi_client.models.host_table_get200_response import HostTableGet200Response
from openapi_client.models.ip_route_table import IpRouteTable
from openapi_client.models.ip_route_table_get200_response import (
    IpRouteTableGet200Response,
)
from openapi_client.models.ipdscp_queue_map_get200_response import (
    IpdscpQueueMapGet200Response,
)
from openapi_client.models.ipdscp_queue_map_get_inner import IpdscpQueueMapGetInner
from openapi_client.models.ipdscp_queue_map_post_request import (
    IpdscpQueueMapPostRequest,
)
from openapi_client.models.lldp_remote_devices import LldpRemoteDevices
from openapi_client.models.lldp_remote_devices_get200_response import (
    LldpRemoteDevicesGet200Response,
)
from openapi_client.models.lldp_remote_devices_mgmt_addresses_inner import (
    LldpRemoteDevicesMgmtAddressesInner,
)
from openapi_client.models.login_post200_response import LoginPost200Response
from openapi_client.models.login_post_request import LoginPostRequest
from openapi_client.models.login_request import LoginRequest
from openapi_client.models.login_token import LoginToken
from openapi_client.models.logout_post200_response import LogoutPost200Response
from openapi_client.models.msti_get200_response import MstiGet200Response
from openapi_client.models.msti_get_inner import MstiGetInner
from openapi_client.models.msti_get_inner_vlans_inner import MstiGetInnerVlansInner
from openapi_client.models.msti_post import MstiPost
from openapi_client.models.msti_post_request import MstiPostRequest
from openapi_client.models.ping_test_start import PingTestStart
from openapi_client.models.ping_test_start_post_request import PingTestStartPostRequest
from openapi_client.models.ping_test_status import PingTestStatus
from openapi_client.models.ping_test_status_get200_response import (
    PingTestStatusGet200Response,
)
from openapi_client.models.poe_config_get import PoeConfigGet
from openapi_client.models.poe_config_get200_response import PoeConfigGet200Response
from openapi_client.models.poe_config_post import PoeConfigPost
from openapi_client.models.poe_config_post_request import PoeConfigPostRequest
from openapi_client.models.ptpv2_get import Ptpv2Get
from openapi_client.models.ptpv2_get200_response import Ptpv2Get200Response
from openapi_client.models.ptpv2_global import Ptpv2Global
from openapi_client.models.ptpv2_global_get200_response import Ptpv2GlobalGet200Response
from openapi_client.models.ptpv2_global_post_request import Ptpv2GlobalPostRequest
from openapi_client.models.ptpv2_post import Ptpv2Post
from openapi_client.models.ptpv2_post_request import Ptpv2PostRequest
from openapi_client.models.snooping_config_get import SnoopingConfigGet
from openapi_client.models.snooping_config_get200_response import (
    SnoopingConfigGet200Response,
)
from openapi_client.models.snooping_config_post import SnoopingConfigPost
from openapi_client.models.snooping_config_post_request import SnoopingConfigPostRequest
from openapi_client.models.snooping_interfaces_get200_response import (
    SnoopingInterfacesGet200Response,
)
from openapi_client.models.snooping_interfaces_get_inner import (
    SnoopingInterfacesGetInner,
)
from openapi_client.models.snooping_interfaces_post import SnoopingInterfacesPost
from openapi_client.models.snooping_interfaces_post_request import (
    SnoopingInterfacesPostRequest,
)
from openapi_client.models.snooping_queriers_get import SnoopingQueriersGet
from openapi_client.models.snooping_queriers_get200_response import (
    SnoopingQueriersGet200Response,
)
from openapi_client.models.snooping_queriers_post import SnoopingQueriersPost
from openapi_client.models.snooping_queriers_post_request import (
    SnoopingQueriersPostRequest,
)
from openapi_client.models.snooping_vlan_get200_response import (
    SnoopingVlanGet200Response,
)
from openapi_client.models.snooping_vlan_inner import SnoopingVlanInner
from openapi_client.models.stp import Stp
from openapi_client.models.stp_get200_response import StpGet200Response
from openapi_client.models.stp_post_request import StpPostRequest
from openapi_client.models.sw_lag_cfg import SwLagCfg
from openapi_client.models.sw_lag_cfg_get200_response import SwLagCfgGet200Response
from openapi_client.models.sw_lag_cfg_post_request import SwLagCfgPostRequest
from openapi_client.models.sw_portmirroring import SwPortmirroring
from openapi_client.models.sw_portmirroring_get200_response import (
    SwPortmirroringGet200Response,
)
from openapi_client.models.sw_portmirroring_post_request import (
    SwPortmirroringPostRequest,
)
from openapi_client.models.sw_portmirroring_src_port_inner import (
    SwPortmirroringSrcPortInner,
)
from openapi_client.models.sw_portstats import SwPortstats
from openapi_client.models.sw_portstats_get200_response import SwPortstatsGet200Response
from openapi_client.models.sw_portstats_get_portid_parameter import (
    SwPortstatsGetPortidParameter,
)
from openapi_client.models.sw_portstats_neighbor_info import SwPortstatsNeighborInfo
from openapi_client.models.swcfg_poe import SwcfgPoe
from openapi_client.models.swcfg_poe_get200_response import SwcfgPoeGet200Response
from openapi_client.models.swcfg_poe_post_request import SwcfgPoePostRequest
from openapi_client.models.swcfg_port import SwcfgPort
from openapi_client.models.swcfg_port_get200_response import SwcfgPortGet200Response
from openapi_client.models.swcfg_port_rtlimit_bcast import SwcfgPortRtlimitBcast
from openapi_client.models.swcfg_port_rtlimit_mcast import SwcfgPortRtlimitMcast
from openapi_client.models.swcfg_port_rtlimit_ucast import SwcfgPortRtlimitUcast
from openapi_client.models.swcfg_vlan import SwcfgVlan
from openapi_client.models.swcfg_vlan_get200_response import SwcfgVlanGet200Response
from openapi_client.models.swcfg_vlan_igmp_config import SwcfgVlanIgmpConfig
from openapi_client.models.swcfg_vlan_membership import SwcfgVlanMembership
from openapi_client.models.swcfg_vlan_membership_get200_response import (
    SwcfgVlanMembershipGet200Response,
)
from openapi_client.models.swcfg_vlan_membership_post_request import (
    SwcfgVlanMembershipPostRequest,
)
from openapi_client.models.swcfg_vlan_membership_pvid_members_inner import (
    SwcfgVlanMembershipPvidMembersInner,
)
from openapi_client.models.swcfg_vlan_membership_traffic_prio_lag_mem_inner import (
    SwcfgVlanMembershipTrafficPrioLagMemInner,
)
from openapi_client.models.swcfg_vlan_membership_traffic_prio_port_mem_inner import (
    SwcfgVlanMembershipTrafficPrioPortMemInner,
)
from openapi_client.models.swcfg_vlan_post_request import SwcfgVlanPostRequest
from openapi_client.models.system_config_get import SystemConfigGet
from openapi_client.models.system_config_get200_response import (
    SystemConfigGet200Response,
)
from openapi_client.models.system_config_post import SystemConfigPost
from openapi_client.models.system_config_post_request import SystemConfigPostRequest
from openapi_client.models.system_rfc1213_get import SystemRfc1213Get
from openapi_client.models.system_rfc1213_get200_response import (
    SystemRfc1213Get200Response,
)
from openapi_client.models.system_rfc1213_post import SystemRfc1213Post
from openapi_client.models.system_rfc1213_post_request import SystemRfc1213PostRequest
from openapi_client.models.traceroute_start import TracerouteStart
from openapi_client.models.traceroute_start_post_request import (
    TracerouteStartPostRequest,
)
from openapi_client.models.traceroute_status import TracerouteStatus
from openapi_client.models.traceroute_status_get200_response import (
    TracerouteStatusGet200Response,
)
from openapi_client.models.vlan_ip import VlanIp
from openapi_client.models.vlan_ip_configuration import VlanIpConfiguration
from openapi_client.models.vlan_ip_get200_response import VlanIpGet200Response
from openapi_client.models.vlan_ip_post_request import VlanIpPostRequest
from openapi_client.models.voice_vlan_cfg import VoiceVlanCfg
from openapi_client.models.voice_vlan_glb_cfg import VoiceVlanGlbCfg
