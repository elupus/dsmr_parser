from dsmr_parser import obis_references as obis

"""
dsmr_parser.obis_name_mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains a mapping of obis references to names.
"""

EN = {
    obis.P1_MESSAGE_HEADER: 'P1_MESSAGE_HEADER',
    obis.P1_MESSAGE_TIMESTAMP: 'P1_MESSAGE_TIMESTAMP',
    obis.ELECTRICITY_IMPORTED_TOTAL: 'ELECTRICITY_IMPORTED_TOTAL',
    obis.ELECTRICITY_REACTIVE_IMPORTED_TOTAL: 'ELECTRICITY_REACTIVE_IMPORTED_TOTAL',
    obis.ELECTRICITY_USED_TARIFF_1: 'ELECTRICITY_USED_TARIFF_1',
    obis.ELECTRICITY_USED_TARIFF_2: 'ELECTRICITY_USED_TARIFF_2',
    obis.ELECTRICITY_EXPORTED_TOTAL: 'ELECTRICITY_EXPORTED_TOTAL',
    obis.ELECTRICITY_REACTIVE_EXPORTED_TOTAL: 'ELECTRICITY_REACTIVE_EXPORTED_TOTAL',
    obis.ELECTRICITY_DELIVERED_TARIFF_1: 'ELECTRICITY_DELIVERED_TARIFF_1',
    obis.ELECTRICITY_DELIVERED_TARIFF_2: 'ELECTRICITY_DELIVERED_TARIFF_2',
    obis.ELECTRICITY_ACTIVE_TARIFF: 'ELECTRICITY_ACTIVE_TARIFF',
    obis.CURRENT_REACTIVE_EXPORTED: 'CURRENT_REACTIVE_EXPORTED',
    obis.ELECTRICITY_REACTIVE_IMPORTED_TARIFF_1: 'ELECTRICITY_REACTIVE_IMPORTED_TARIFF_1',
    obis.ELECTRICITY_REACTIVE_IMPORTED_TARIFF_2: 'ELECTRICITY_REACTIVE_IMPORTED_TARIFF_2',
    obis.ELECTRICITY_REACTIVE_EXPORTED_TARIFF_1: 'ELECTRICITY_REACTIVE_EXPORTED_TARIFF_1',
    obis.ELECTRICITY_REACTIVE_EXPORTED_TARIFF_2: 'ELECTRICITY_REACTIVE_EXPORTED_TARIFF_2',
    obis.CURRENT_REACTIVE_IMPORTED: 'CURRENT_REACTIVE_IMPORTED',
    obis.EQUIPMENT_IDENTIFIER: 'EQUIPMENT_IDENTIFIER',
    obis.CURRENT_ELECTRICITY_USAGE: 'CURRENT_ELECTRICITY_USAGE',
    obis.CURRENT_ELECTRICITY_DELIVERY: 'CURRENT_ELECTRICITY_DELIVERY',
    obis.LONG_POWER_FAILURE_COUNT: 'LONG_POWER_FAILURE_COUNT',
    obis.SHORT_POWER_FAILURE_COUNT: 'SHORT_POWER_FAILURE_COUNT',
    obis.POWER_EVENT_FAILURE_LOG: 'POWER_EVENT_FAILURE_LOG',
    obis.VOLTAGE_SAG_L1_COUNT: 'VOLTAGE_SAG_L1_COUNT',
    obis.VOLTAGE_SAG_L2_COUNT: 'VOLTAGE_SAG_L2_COUNT',
    obis.VOLTAGE_SAG_L3_COUNT: 'VOLTAGE_SAG_L3_COUNT',
    obis.VOLTAGE_SWELL_L1_COUNT: 'VOLTAGE_SWELL_L1_COUNT',
    obis.VOLTAGE_SWELL_L2_COUNT: 'VOLTAGE_SWELL_L2_COUNT',
    obis.VOLTAGE_SWELL_L3_COUNT: 'VOLTAGE_SWELL_L3_COUNT',
    obis.INSTANTANEOUS_VOLTAGE_L1: 'INSTANTANEOUS_VOLTAGE_L1',
    obis.INSTANTANEOUS_VOLTAGE_L2: 'INSTANTANEOUS_VOLTAGE_L2',
    obis.INSTANTANEOUS_VOLTAGE_L3: 'INSTANTANEOUS_VOLTAGE_L3',
    obis.INSTANTANEOUS_CURRENT_L1: 'INSTANTANEOUS_CURRENT_L1',
    obis.INSTANTANEOUS_CURRENT_L2: 'INSTANTANEOUS_CURRENT_L2',
    obis.INSTANTANEOUS_CURRENT_L3: 'INSTANTANEOUS_CURRENT_L3',
    obis.TEXT_MESSAGE_CODE: 'TEXT_MESSAGE_CODE',
    obis.TEXT_MESSAGE: 'TEXT_MESSAGE',
    obis.DEVICE_TYPE: 'DEVICE_TYPE',
    obis.INSTANTANEOUS_ACTIVE_POWER_L1_POSITIVE: 'INSTANTANEOUS_ACTIVE_POWER_L1_POSITIVE',
    obis.INSTANTANEOUS_ACTIVE_POWER_L2_POSITIVE: 'INSTANTANEOUS_ACTIVE_POWER_L2_POSITIVE',
    obis.INSTANTANEOUS_ACTIVE_POWER_L3_POSITIVE: 'INSTANTANEOUS_ACTIVE_POWER_L3_POSITIVE',
    obis.INSTANTANEOUS_ACTIVE_POWER_L1_NEGATIVE: 'INSTANTANEOUS_ACTIVE_POWER_L1_NEGATIVE',
    obis.INSTANTANEOUS_ACTIVE_POWER_L2_NEGATIVE: 'INSTANTANEOUS_ACTIVE_POWER_L2_NEGATIVE',
    obis.INSTANTANEOUS_ACTIVE_POWER_L3_NEGATIVE: 'INSTANTANEOUS_ACTIVE_POWER_L3_NEGATIVE',
    obis.INSTANTANEOUS_REACTIVE_POWER_L1_POSITIVE: 'INSTANTANEOUS_REACTIVE_POWER_L1_POSITIVE',
    obis.INSTANTANEOUS_REACTIVE_POWER_L1_NEGATIVE: 'INSTANTANEOUS_REACTIVE_POWER_L1_NEGATIVE',
    obis.INSTANTANEOUS_REACTIVE_POWER_L2_POSITIVE: 'INSTANTANEOUS_REACTIVE_POWER_L2_POSITIVE',
    obis.INSTANTANEOUS_REACTIVE_POWER_L2_NEGATIVE: 'INSTANTANEOUS_REACTIVE_POWER_L2_NEGATIVE',
    obis.INSTANTANEOUS_REACTIVE_POWER_L3_POSITIVE: 'INSTANTANEOUS_REACTIVE_POWER_L3_POSITIVE',
    obis.INSTANTANEOUS_REACTIVE_POWER_L3_NEGATIVE: 'INSTANTANEOUS_REACTIVE_POWER_L3_NEGATIVE',
    obis.EQUIPMENT_IDENTIFIER_GAS: 'EQUIPMENT_IDENTIFIER_GAS',
    obis.HOURLY_GAS_METER_READING: 'HOURLY_GAS_METER_READING',
    obis.GAS_METER_READING: 'GAS_METER_READING',
    obis.ACTUAL_TRESHOLD_ELECTRICITY: 'ACTUAL_TRESHOLD_ELECTRICITY',
    obis.ACTUAL_SWITCH_POSITION: 'ACTUAL_SWITCH_POSITION',
    obis.VALVE_POSITION_GAS: 'VALVE_POSITION_GAS',
    obis.BELGIUM_VERSION_INFORMATION: 'BELGIUM_VERSION_INFORMATION',
    obis.BELGIUM_EQUIPMENT_IDENTIFIER: 'BELGIUM_EQUIPMENT_IDENTIFIER',
    obis.BELGIUM_CURRENT_AVERAGE_DEMAND: 'BELGIUM_CURRENT_AVERAGE_DEMAND',
    obis.BELGIUM_MAXIMUM_DEMAND_MONTH: 'BELGIUM_MAXIMUM_DEMAND_MONTH',
    obis.BELGIUM_MAXIMUM_DEMAND_13_MONTHS: 'BELGIUM_MAXIMUM_DEMAND_13_MONTHS',
    obis.BELGIUM_MAX_POWER_PER_PHASE: 'BELGIUM_MAX_POWER_PER_PHASE',
    obis.BELGIUM_MAX_CURRENT_PER_PHASE: 'BELGIUM_MAX_CURRENT_PER_PHASE',
    obis.BELGIUM_MBUS1_DEVICE_TYPE: 'BELGIUM_MBUS1_DEVICE_TYPE',
    obis.BELGIUM_MBUS1_EQUIPMENT_IDENTIFIER: 'BELGIUM_MBUS1_EQUIPMENT_IDENTIFIER',
    obis.BELGIUM_MBUS1_VALVE_POSITION: 'BELGIUM_MBUS1_VALVE_POSITION',
    obis.BELGIUM_MBUS1_METER_READING1: 'BELGIUM_MBUS1_METER_READING1',
    obis.BELGIUM_MBUS1_METER_READING2: 'BELGIUM_MBUS1_METER_READING2',
    obis.BELGIUM_MBUS2_EQUIPMENT_IDENTIFIER: 'BELGIUM_MBUS2_EQUIPMENT_IDENTIFIER',
    obis.BELGIUM_MBUS2_VALVE_POSITION: 'BELGIUM_MBUS2_VALVE_POSITION',
    obis.BELGIUM_MBUS2_METER_READING1: 'BELGIUM_MBUS2_METER_READING1',
    obis.BELGIUM_MBUS2_METER_READING2: 'BELGIUM_MBUS2_METER_READING2',
    obis.BELGIUM_MBUS3_EQUIPMENT_IDENTIFIER: 'BELGIUM_MBUS3_EQUIPMENT_IDENTIFIER',
    obis.BELGIUM_MBUS3_VALVE_POSITION: 'BELGIUM_MBUS3_VALVE_POSITION',
    obis.BELGIUM_MBUS3_METER_READING1: 'BELGIUM_MBUS3_METER_READING1',
    obis.BELGIUM_MBUS3_METER_READING2: 'BELGIUM_MBUS3_METER_READING2',
    obis.BELGIUM_MBUS4_EQUIPMENT_IDENTIFIER: 'BELGIUM_MBUS4_EQUIPMENT_IDENTIFIER',
    obis.BELGIUM_MBUS4_VALVE_POSITION: 'BELGIUM_MBUS4_VALVE_POSITION',
    obis.BELGIUM_MBUS4_METER_READING1: 'BELGIUM_MBUS4_METER_READING1',
    obis.BELGIUM_MBUS4_METER_READING2: 'BELGIUM_MBUS4_METER_READING2',
    obis.LUXEMBOURG_EQUIPMENT_IDENTIFIER: 'LUXEMBOURG_EQUIPMENT_IDENTIFIER',
    obis.Q3D_EQUIPMENT_IDENTIFIER: 'Q3D_EQUIPMENT_IDENTIFIER',
    obis.Q3D_EQUIPMENT_STATE: 'Q3D_EQUIPMENT_STATE',
    obis.Q3D_EQUIPMENT_SERIALNUMBER: 'Q3D_EQUIPMENT_SERIALNUMBER',
    obis.BELGIUM_MBUS2_DEVICE_TYPE: 'BELGIUM_MBUS2_DEVICE_TYPE'
}

REVERSE_EN = dict([(v, k) for k, v in EN.items()])
