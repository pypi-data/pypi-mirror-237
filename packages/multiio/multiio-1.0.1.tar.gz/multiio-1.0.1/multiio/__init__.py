#!/usr/bin/python3

from smbus2 import SMBus
import struct
import datetime

_CARD_NAME = "Multi-IO"
_PROGRAM_NAME = "multiio"
_VERSION = "1.0.1"

_SLAVE_OWN_ADDRESS_BASE = 0x06
_STACK_LEVEL_MAX = 7

_CHANNEL_NO = {
    "motor": 1,
    "opto": 4,
    "opto_enc": 4 / 2,
    "adc": 3,
    "i_in": 2,
    "u_in": 2,
    "i_out": 2,
    "u_out": 2,
    "rtd": 2,
    "led": 6,
    "relay": 2,
    "servo": 2,
}

_COUNTER_SIZE = 4
_ADC_RAW_CHANNELS = 5
_ADC_RAW_VAL_SIZE = 2
_ANALOG_VAL_SIZE = 2
_SERVO_VAL_SIZE = 2
_RTD_TEMP_DATA_SIZE = 4
_RTD_RES_DATA_SIZE = 4

_CALIBRATION_KEY = 0xaa
_RESET_CALIBRATION_KEY  = 0x55
_WDT_RESET_SIGNATURE     = 0xca
_WDT_RESET_COUNT_SIGNATURE    = 0xbe

_VOLT_TO_MILIVOLT = 1000
_MILIAMPER_TO_MICROAMPER = 1000

_CALIB_IN_PROGRESS = 0
_CALIB_DONE = 1
_CALIB_ERROR = 2
_CALIB_NOTHING = 0
_CALIB_RTD_CH1 = 1
_CALIB_U_IN_CH1 = 3
_CALIB_I_IN_CH1 = 5
_CALIB_U_OUT_CH1 = 7
_CALIB_I_OUT_CH1 = 9
_CALIB_LAST_CH = 10

# i2c memory addresses
_I2C_MEM_RELAYS = 0
_I2C_MEM_RELAY_SET = 1
_I2C_MEM_RELAY_CLR = 2
_I2C_MEM_LEDS = 3
_I2C_MEM_LED_SET = 4
_I2C_MEM_LED_CLR = 5
_I2C_MEM_OPTO = 6
_I2C_MEM_ANALOG_TYPE = 7
_I2C_MEM_U_IN = 8
_I2C_MEM_I_IN = 12
_I2C_MEM_U_OUT = 16
_I2C_MEM_I_OUT = 20
_I2C_MEM_MOT_VAL = 24
_I2C_MEM_SERVO_VAL1 = 26
_I2C_MEM_SERVO_VAL2 = 28
_I2C_MEM_RTD_VAL1_ADD = 30
_I2C_MEM_RTD_RES1_ADD = 38
_I2C_MEM_DIAG_TEMPERATURE_ADD = 46
_I2C_MEM_DIAG_3V3_MV_ADD = 47
_I2C_MEM_DIAG_3V3_MV_ADD1 = 48
_I2C_MEM_OPTO_IT_RISING_ADD = 49
_I2C_MEM_OPTO_IT_FALLING_ADD = 50
_I2C_MEM_OPTO_ENC_ENABLE_ADD = 51
_I2C_MEM_OPTO_CNT_RST_ADD = 52
_I2C_MEM_OPTO_ENC_CNT_RST_ADD = 53
_I2C_MEM_OPTO_EDGE_COUNT_ADD = 54
_I2C_MEM_OPTO_ENC_COUNT_ADD = 70
_I2C_MEM_CALIB_VALUE = 78
_I2C_MEM_CALIB_CHANNEL = 82
_I2C_MEM_CALIB_KEY = 83
_I2C_MEM_CALIB_STATUS = 84
_I2C_RTC_YEAR_ADD = 85
_I2C_RTC_MONTH_ADD = 86
_I2C_RTC_DAY_ADD = 87
_I2C_RTC_HOUR_ADD = 88
_I2C_RTC_MINUTE_ADD = 89
_I2C_RTC_SECOND_ADD = 90
_I2C_RTC_SET_YEAR_ADD = 91
_I2C_RTC_SET_MONTH_ADD = 92
_I2C_RTC_SET_DAY_ADD = 93
_I2C_RTC_SET_HOUR_ADD = 94
_I2C_RTC_SET_MINUTE_ADD = 95
_I2C_RTC_SET_SECOND_ADD = 96
_I2C_RTC_CMD_ADD = 97
_I2C_MEM_WDT_RESET_ADD = 98
_I2C_MEM_WDT_INTERVAL_SET_ADD = 99
_I2C_MEM_WDT_INTERVAL_GET_ADD = 101
_I2C_MEM_WDT_INIT_INTERVAL_SET_ADD = 103
_I2C_MEM_WDT_INIT_INTERVAL_GET_ADD = 105
_I2C_MEM_WDT_RESET_COUNT_ADD = 107
_I2C_MEM_WDT_CLEAR_RESET_COUNT_ADD = 109
_I2C_MEM_WDT_POWER_OFF_INTERVAL_SET_ADD = 110
_I2C_MEM_WDT_POWER_OFF_INTERVAL_GET_ADD = 111
_I2C_MEM_REVISION_HW_MAJOR_ADD = 0x78
_I2C_MEM_REVISION_HW_MINOR_ADD = _I2C_MEM_REVISION_HW_MAJOR_ADD + 1
_I2C_MEM_REVISION_MAJOR_ADD = _I2C_MEM_REVISION_HW_MINOR_ADD + 1
_I2C_MEM_REVISION_MINOR_ADD = _I2C_MEM_REVISION_HW_MAJOR_ADD + 1
_I2C_MEM_BUTTON = 0xff # TODO
_SLAVE_BUFF_SIZE = 255

ON = 0
OFF = 1
STATE_COUNT = 2

class SMmultiio:
    def __init__(self, stack=0, i2c=1):
        if stack < 0 or stack > _STACK_LEVEL_MAX:
            raise ValueError('Invalid stack level!')
        self._hw_address_ = _SLAVE_OWN_ADDRESS_BASE + stack
        self._i2c_bus_no = i2c
        self.bus = SMBus(self._i2c_bus_no)
        try:
            self._card_rev_major = self.bus.read_byte_data(self._hw_address_, _I2C_MEM_REVISION_HW_MAJOR_ADD)
            self._card_rev_minor = self.bus.read_byte_data(self._hw_address_, _I2C_MEM_REVISION_HW_MINOR_ADD)
        except Exception:
            print("{} not detected!".format(_CARD_NAME))
            raise

    def get_byte(self, address):
        return self.bus.read_byte_data(self._hw_address_, address)
    def get_word(self, address):
        return self.bus.read_word_data(self._hw_address_, address)
    def get_i16(self, address):
        buf = self.bus.read_i2c_block_data(self._hw_address_, address, 2)
        i16_value = struct.unpack("h", bytearray(buf))[0]
        return i16_value
    def get_float(self, address):
        buf = self.bus.read_i2c_block_data(self._hw_address_, address, 4)
        float_value = struct.unpack("f", bytearray(buf))[0]
        return float_value
    def get_i32(self, address):
        buf = self.bus.read_i2c_block_data(self._hw_address_, address, 4)
        i32_value = struct.unpack("i", bytearray(buf))[0]
        return i32_value
    def get_u32(self, address):
        buf = self.bus.read_i2c_block_data(self._hw_address_, address, 4)
        u32_value = struct.unpack("I", bytearray(buf))[0]
        return u32_value
    def get_block_data(self, address, byteno=4):
        return self.bus.read_i2c_block_data(self._hw_address_, address, byteno)
    def set_byte(self, address, value):
        self.bus.write_byte_data(self._hw_address_, address, value)
    def set_word(self, address, value):
        self.bus.write_word_data(self._hw_address_, address, value)
    def set_float(self, address, value):
        ba = bytearray(struct.pack("f", value))
        self.bus.write_block_data(self._hw_address_, address, ba)
    def set_i32(self, address, value):
        ba = bytearray(struct.pack("i", value))
        self.bus.write_block_data(self._hw_address_, address, ba)
    def set_block(self, address, ba):
        self.bus.write_i2c_block_data(self._hw_address_, address, ba)

    @staticmethod
    def check_channel(channel_type, channel):
        if not (0 <= channel and channel <= _CHANNEL_NO[channel_type]):
            raise ValueError('Invalid {} channel number. Must be [1..{}]!'.format(channel_type, _CHANNEL_NO[channel_type]))
    def _calib_set(self, channel, value):
        ba = bytearray(struct.pack("f", value))
        ba.extend([channel, _CALIBRATION_KEY])
        self.set_block(_I2C_MEM_CALIB_VALUE, ba)

    def _calib_reset(self, channel):
        ba = bytearray([channel, _CALIBRATION_KEY])
        self.set_block(_I2C_MEM_CALIB_CHANNEL, ba)

    def calib_status(self):
        status = self.get_byte(_I2C_MEM_CALIB_STATUS)
        return status

    def get_version(self):
        version_major = self.get_byte(_I2C_MEM_REVISION_MAJOR_ADD)
        version_minor = self.get_byte(_I2C_MEM_REVISION_MINOR_ADD)
        version = str(version_major) + "." + str(version_minor)
        return version

    def get_relay(self, relay):
        self.check_channel("relay", relay)
        val = self.get_byte(_I2C_MEM_RELAYS)
        if (val & (1 << (relay - 1))) != 0:
            return 1
        return 0
    def get_all_relays(self):
        val = self.get_byte(_I2C_MEM_RELAYS)
        return val
    def set_relay(self, relay, val):
        self.check_channel("relay", relay)
        if val != 0:
            self.set_byte(_I2C_MEM_RELAY_SET, relay)
        else:
            self.set_byte(_I2C_MEM_RELAY_CLR, relay)
    def set_all_relays(self, val):
        if(not (0 <= val and val <= (1 << _CHANNEL_NO["relay"]) - 1)):
            raise ValueError('Invalid relay mask')
        self.set_byte(_I2C_MEM_RELAYS, 0xff & val)

    def get_u_in(self, channel):
        self.check_channel("u_in", channel)
        value = self.get_word(_I2C_MEM_U_IN + (channel - 1) * 2)
        return value / _VOLT_TO_MILIVOLT
    def cal_u_in(self, channel, value):
        self.check_channel("u_in", channel)
        self._calib_set(_CALIB_U_IN_CH1 + channel, value)
    def get_u_out(self, channel):
        self.check_channel("u_out", channel)
        value = self.get_word(_I2C_MEM_U_OUT + (channel - 1) * 2)
        return value / _VOLT_TO_MILIVOLT
    def set_u_out(self, channel, value):
        self.check_channel("u_out", channel)
        value = value * _VOLT_TO_MILIVOLT
        self.set_word(_I2C_MEM_U_OUT + (channel - 1) * 2, value)
    def cal_u_out(self, channel, value):
        self.check_channel("u_out", channel)
        self._calib_set(_CALIB_U_OUT_CH1 + channel, value)

    def get_i_in(self, channel):
        self.check_channel("i_in", channel)
        value = self.get_word(_I2C_MEM_I_IN + (channel - 1) * 2)
        return value / _VOLT_TO_MILIVOLT
    def cal_i_in(self, channel, value):
        self.check_channel("i_in", channel)
        self._calib_set(_CALIB_I_IN_CH1 + channel, value)
    def get_i_out(self, channel):
        self.check_channel("i_out", channel)
        value = self.get_word(_I2C_MEM_I_OUT + (channel - 1) * 2)
        return value / _VOLT_TO_MILIVOLT
    def set_i_out(self, channel, value):
        self.check_channel("i_out", channel)
        value = value * _VOLT_TO_MILIVOLT
        self.set_word(_I2C_MEM_I_OUT + (channel - 1) * 2, value)
    def cal_i_out(self, channel, value):
        self.check_channel("i_out", channel)
        self._calib_set(_CALIB_I_OUT_CH1 + channel, value)

    def get_rtd_res(self, channel):
        self.check_channel("rtd", channel)
        return self.get_float(_I2C_MEM_RTD_RES1_ADD + (channel - 1) * 4)
    def get_rtd_temp(self, channel):
        self.check_channel("rtd", channel)
        return self.get_float(_I2C_MEM_RTD_VAL1_ADD + (channel - 1) * 4)
    def cal_rtd_res(self, channel, value):
        self.check_channel("rtd", channel)
        self._calib_set(_CALIB_RTD_CH1 + channel - 1, value)

    def get_led(self, led):
        self.check_channel("led", led)
        val = self.get_byte(_I2C_MEM_LEDS)
        if (val & (1 << (led - 1))) != 0:
            return 1
        return 0
    def get_all_leds(self):
        return self.get_byte(_I2C_MEM_LEDS)
    def set_led(self, led, val):
        self.check_channel("led", led)
        if val != 0:
            self.set_byte(_I2C_MEM_LED_SET, led)
        else:
            self.set_byte(_I2C_MEM_LED_CLR, led)
    def set_all_leds(self, val):
        self.set_byte(_I2C_MEM_LEDS, 0xff & val)

    def wdt_reload(self):
        self.set_byte(_I2C_MEM_WDT_RESET_ADD, _WDT_RESET_SIGNATURE)
    def wdt_get_period(self):
        return self.get_word(_I2C_MEM_WDT_INTERVAL_GET_ADD)
    def wdt_set_period(self, period):
        return self.set_word(_I2C_MEM_WDT_INTERVAL_SET_ADD, period)
    def wdt_get_init_period(self):
        return self.get_word(_I2C_MEM_WDT_INIT_INTERVAL_GET_ADD)
    def wdt_set_init_period(self, period):
        return self.set_word(_I2C_MEM_WDT_INIT_INTERVAL_SET_ADD, period)

    def wdt_get_off_period(self):
        return self.get_i32(_I2C_MEM_WDT_POWER_OFF_INTERVAL_GET_ADD)
    def wdt_set_off_period(self, period):
        return self.set_i32(_I2C_MEM_WDT_POWER_OFF_INTERVAL_SET_ADD, period)
    def wdt_get_reset_count(self):
        return self.get_word(_I2C_MEM_WDT_RESET_COUNT_ADD)
    def wdt_clear_reset_count(self):
        return self.set_i32(_I2C_MEM_WDT_CLEAR_RESET_COUNT_ADD, _WDT_RESET_COUNT_SIGNATURE)

    def get_rtc(self):
        buf = self.get_block_data(_I2C_RTC_YEAR_ADD, 6)
        buf[0] += 2000
        return tuple(buf)
    def set_rtc(self, year, month, day, hour, minute, second):
        if year > 2000:
            year -= 2000
        if(not(0 <= year and year <= 255)):
            raise ValueError("Invalid year!")
        datetime.datetime(
                year=2000+year, month=month, day=day,
                hour=hour, minute=minute, second=second)
        ba = bytearray(struct.pack(
            "6B B",
            year, month, day, hour, minute, second,
            _CALIBRATION_KEY))
        print(ba)
        self.set_block(_I2C_RTC_SET_YEAR_ADD, ba)
    def get_opto(self, channel):
        self.check_channel("opto", channel)
        opto_mask = self.get_byte(_I2C_MEM_OPTO)
        if(opto_mask & (1 << (channel - 1))):
            return True
        else:
            return False
    def get_all_opto(self):
        return self.get_byte(_I2C_MEM_OPTO)
    def get_opto_edge(self, channel):
        self.check_channel("opto", channel)
        rising = self.get_byte(_I2C_MEM_OPTO_IT_RISING_ADD)
        falling = self.get_byte(_I2C_MEM_OPTO_IT_FALLING_ADD)
        channel_bit = 1 << (channel - 1)
        value = 0
        if(rising & channel_bit):
            value |= 1
        if(falling & channel_bit):
            value |= 2
        return value
    def set_opto_edge(self, channel, value):
        self.check_channel("opto", channel)
        rising = self.get_byte(_I2C_MEM_OPTO_IT_RISING_ADD)
        falling = self.get_byte(_I2C_MEM_OPTO_IT_FALLING_ADD)
        channel_bit = 1 << (channel - 1)
        if(value & 1):
            rising |= channel_bit
        else:
            rising &= ~channel_bit
        if(value & 2):
            falling |= channel_bit
        else:
            rising &= ~channel_bit
        self.set_byte(_I2C_MEM_OPTO_IT_RISING_ADD, rising)
        self.set_byte(_I2C_MEM_OPTO_IT_FALLING_ADD, falling)
    def get_opto_counter(self, channel):
        self.check_channel("opto", channel)
        return self.get_u32(_I2C_MEM_OPTO_EDGE_COUNT_ADD + (channel - 1) * 4)
    def reset_opto_counter(self, channel):
        self.check_channel("opto", channel)
        return self.set_byte(_I2C_MEM_OPTO_CNT_RST_ADD, channel)
    def get_opto_encoder_state(self, channel):
        self.check_channel("opto_enc", channel)
        encoder_mask = self.get_byte(_I2C_MEM_OPTO_ENC_ENABLE_ADD)
        channel_bit = 1 << (channel - 1)
        if(encoder_mask & channel_bit):
            return True
        else:
            return False
    def set_opto_encoder_state(self, channel, value):
        self.check_channel("opto_enc", channel)
        encoder_mask = self.get_byte(_I2C_MEM_OPTO_ENC_ENABLE_ADD)
        channel_bit = 1 << (channel - 1)
        if(value == 1):
            encoder_mask |= channel_bit
        elif(value == 0):
            encoder_mask &= ~channel_bit
        else:
            raise ValueError("Invalid value! Must be 0 or 1!")
        self.set_byte(_I2C_MEM_OPTO_ENC_ENABLE_ADD, encoder_mask)
    def get_opto_encoder_counter(self, channel):
        self.check_channel("opto_enc", channel)
        return self.get_i32(_I2C_MEM_OPTO_ENC_COUNT_ADD + (channel - 1) * 4)
    def reset_opto_encoder_counter(self, channel):
        self.check_channel("opto_enc", channel)
        self.set_byte(_I2C_MEM_OPTO_ENC_CNT_RST_ADD, channel)

    def get_servo(self, channel):
        self.check_channel("servo", channel)
        return self.get_i16(_I2C_MEM_SERVO_VAL1 + (channel - 1) * 2) / 10
    def set_servo(self, channel, value):
        self.check_channel("servo", channel)
        if(not(-140 <= value and value <= 140)):
            raise ValueError("Servo value out of range! Must be [-140..140]")
        self.set_word(_I2C_MEM_SERVO_VAL1 + (channel - 1) * 2, value * 10)

    def get_motor(self, channel):
        self.check_channel("motor", channel)
        return self.get_word(_I2C_MEM_MOT_VAL + (channel - 1) * 2) / 10
    def set_motor(self, channel, value):
        self.check_channel("motor", channel)
        if(not(-100 <= value and value <= 100)):
            raise ValueError("Motor value out of range! Must be [-100..100]")
        self.set_word(_I2C_MEM_MOT_VAL + (channel - 1) * 2, value * 10)

    def get_button(self):
        state = self.get_byte(_I2C_MEM_BUTTON)
        if(state & 1):
            return True
        else:
            return False
    def get_button_latch(self):
        state = self.get_byte(_I2C_MEM_BUTTON)
        if(state & 2):
            state &= ~2
            self.set_byte(_I2C_MEM_BUTTON, state)
            return True
        else:
            return False

multiio = SMmultiio()
