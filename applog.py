import random, time, json, requests, uuid; from collections import OrderedDict


class Applog():
    def __init__(self) -> None:
        pass

    def get_payload(self):
        self.mc         = f'{random.randint(1, 9)}{random.randint(1, 9)}:{random.randint(1, 9)}9:8A:7{random.randint(1, 9)}:{random.randint(1, 9)}{random.randint(1, 9)}:{random.randint(1, 9)}{random.randint(1, 9)}'
        self.serialnum  = f'{random.randint(1, 9)}abd{random.randint(1, 9)}ec{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}f'
        self.googleaid  = str(uuid.uuid4())
        self.clientudid = str(random.randint(100000000000000, 999999999999999))
        self.openudid  = str(random.randint(1000000000000000, 9999999999999999))
        self.osversion  = f'{random.randint(4, 5)}.{random.randint(0, 9)}.{random.randint(0, 9)}'
        self.appversion = '9.1.0'
        self.dev_brand  = 'samsung'
        self.dev_model  = 'Galaxy J'

        Data = OrderedDict(
            [
                (
                    'header',
                    OrderedDict(
                        [
                            ('appkey', '57bfa27c67e58e7d920028d3'),
                            ('serial_number', self.serialnum),
                            ('display_density','mdpi'),
                            ('tz_name','America/New_York'),
                            ('rom','G361HXXU0AQK10'),
                            ('release_build','7f052cf_20181116'),
                            ('resolution','1794x1080'),
                            ('timezone','1'),
                            ('carrier', 'GSM'),
                            ('mcc_mnc','20820'),
                            ('sim_serial_number', OrderedDict([])),
                            ('rom_version','OPM6.171019.030.K1'),
                            ('density_dpi','420'),
                            ('device_brand', self.dev_brand),
                            ('manifest_version_code','2018111632'),
                            ('device_manufacturer','LGE'),
                            ('clientudid',self.clientudid),
                            ('openudid', self.openudid),
                            ('update_version_code','2018111632'),
                            ('os_api','28'),
                            ("display_name","musical_ly"),
                            ("app_version","13.1.3"),
                            ("version_code","130103"),
                            ('mc', self.mc),
                            ('language','ru'),
                            ('build_serial', self.serialnum),
                            ('device_model',self.dev_model),
                            ('google_aid',self.googleaid),
                            ('region','RU'),
                            ('package','com.zhiliaoapp.musically'),
                            ('tz_offset','3600'),
                            ('sim_region','ru'),
                            ('access','wifi'),
                            ('os_version', self.osversion),
                            ('sdk_version','4'),
                            ('carrier','Lycamobile'),
                            ('cpu_abi','armeabi-v7a'),
                            ('aid','1233'),
                            ('app_version',self.appversion),
                            ('os','Android'),
                            ('not_request_sender',0),
                            ('channel','wandoujia')])),
                ('_gen_time',int(time.time())),
                ('magic_tag','ss_app_log')
                ]
            )

        return json.dumps(Data)

    def get_device(self):
        payload = self.get_payload()
        
        req = requests.post(
            url = 'http://applog.musical.ly/service/2/device_register/',
            headers = {
                'user-agent': 'okhttp/3.10.0.1'
            },
            data = payload
        )
        return json.dumps(req.json(), indent=4)

if __name__ == "__main__":
    applog = Applog()
    device_id = applog.get_device()

    print(device_id)
