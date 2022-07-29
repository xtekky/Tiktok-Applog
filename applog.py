import random, time, json, requests, uuid; from collections import OrderedDict

class Applog:
    
    def __init__(self) -> None:
        self.mc         = f'{random.randint(1, 9)}{random.randint(1, 9)}:{random.randint(1, 9)}9:8A:7{random.randint(1, 9)}:{random.randint(1, 9)}{random.randint(1, 9)}:{random.randint(1, 9)}{random.randint(1, 9)}'
        self.serialnum  = f'{random.randint(1, 9)}abd{random.randint(1, 9)}ec{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}f'
        self.googleaid  = str(uuid.uuid4())
        self.clientudid = str(random.randint(100000000000000, 999999999999999))
        self.openudid  = str(random.randint(1000000000000000, 9999999999999999))
        self.osversion  = f'{random.randint(4, 5)}.{random.randint(0, 9)}.{random.randint(0, 9)}'
        self.appversion = '19.3.3'
        self.dev_brand  = 'motorola'
        self.dev_model  = 'XT1069'
        self.aid = "1233"
        self.version_code = "2021903030"
        self.timezone = "America/Sao_Paulo"
        self.offset = "3600"
        self.res = "720x1280"
        self.lang = 'pt'
        self.region = "BR"
        self.dpi = "320"
        self.build = "MPB24.65-34-3"
 
    def get_payload(self) -> dict:
 
        data = {
            "header": {
                "serial_number": self.serialnum,
                "display_density": "mdpi",
                "tz_name": self.timezone,
                "resolution": self.res,
                "timezone": "1",
                "carrier": "Lycamobile",
                "sim_serial_number": {},
                "rom_version": self.build, #"MPB24.65-34-3",
                "density_dpi": self.dpi,
                "device_brand": self.dev_brand,
                "manifest_version_code": self.version_code,
                "device_manufacturer": self.dev_brand,
                "clientudid": self.clientudid,
                "openudid": self.openudid,
                "update_version_code": self.version_code,
                "os_api": "23",
                "display_name": "musical_ly",
                "app_version": self.appversion,
                "version_code": str(self.appversion).replace(".", "0"),
                "mc": self.mc,
                "language": self.lang, #"pt_BR",
                "build_serial": self.serialnum,
                "device_model": self.dev_model,
                "google_aid": self.googleaid,
                "region": self.region,
                "package": "com.zhiliaoapp.musically",
                "tz_offset": self.offset,
                "sim_region": "ru",
                "access": "wifi",
                "os_version": self.osversion,
                "sdk_version": "4",
                "cpu_abi": "armeabi-v7a",
                "aid": self.aid,
                "os": "Android",
                "not_request_sender": 0,
                "channel": "wandoujia"
            },
            "_gen_time": int(time.time()),
            "magic_tag": "ss_app_log"
        }
 
        return json.dumps(data)
    
    def get_params(self) -> str:
        params = {
            "ac": "wifi",
            "channel": "googleplay",
            "aid": self.aid,
            "app_name": "musical_ly",
            "version_code": str(self.appversion).replace('.', '0'),
            "version_name": self.appversion,
            "device_platform": "android",
            "ab_version": self.appversion,
            "ssmix": "a",
            "device_type": self.dev_model, #"XT1069",
            "device_brand": self.dev_brand, #"motorola",
            "language": self.lang,
            "os_api": "23",
            "os_version": "6.0",
            "openudid": self.openudid, #"a08b76606458ca0d",
            "manifest_version_code": self.version_code,
            "resolution": "720*1184",
            "dpi": self.dpi,
            "update_version_code": self.version_code,
            "_rticket": str(int(time.time())) + "000",
            "app_type": "normal",
            "sys_region": self.region,
            "timezone_name": self.timezone,
            "ts": int(time.time()),
            "timezone_offset": self.offset,
            "build_number": self.appversion,
            "region": self.region,
            "uoo": "1",
            "app_language": self.lang,
            "locale": f"{self.lang}-{self.region}",
            "op_region": self.region,
            "ac2": "wifi",
            "cdid": self.googleaid #"8e90c714-5b9e-4f23-b1b8-fbedeecb8884"
        }
        
        return urllib.parse.urlencode(params)
    
    def get_headers(self, params: str, payload: dict):
        sig = Xgorgon(params, payload, None).get_value()
        
        headers = {
            "x-ss-stub": str(hashlib.md5(payload.encode()).hexdigest()).upper(),
            "accept-encoding": "gzip",
            "passport-sdk-version": "19",
            "sdk-version": "2",
            "x-ss-req-ticket": str(int(time.time())) + "000",
            "x-tt-dm-status": "login=0;ct=0",
            "host": "log-va.tiktokv.com",
            "connection": "Keep-Alive",
            "user-agent": (
                f"com.zhiliaoapp.musically/{self.version_code} "
                + f"(Linux; U; Android 6.0; pt_BR; {self.dev_model}; "
                + f"Build/{self.build}; "
                + "Cronet/TTNetVersion:5f9640e3 2021-04-21 QuicVersion:47946d2a 2020-10-14)"
            ),
            'X-Gorgon': sig["X-Gorgon"],
            'X-Khronos': sig["X-Khronos"]
        }
        
        return headers
 
    def get_device(self) -> dict:
        payload = self.get_payload()
        params = self.get_params()
        
        req = requests.post(
            url = (
                'http://'
                + 'log-va.tiktokv.com'
                + '/service/2/device_register/?'
                + params
            ),
            headers = self.get_headers(params, payload),
            data = payload
        )
        return json.dumps(req.json(), indent=4)
 
if __name__ == "__main__":
    applog = Applog()
    device_id = applog.get_device()
 
    a = json.loads(device_id)
    print(
        str(
                {
                'device_id': a['device_id'], 
                'install_id': a['install_id']
            }
        )
    )
