import requests,re,time,uuid,os,json,string,random,sys,hashlib
from bs4 import BeautifulSoup as parser
from datetime import date,datetime

D = "\033[91m"
W = "\033[37m"

class login:
    def __init__(self, cokie_tumbal):
        self.cokie = {'cookie':cokie_tumbal}
        self.client = str(uuid.uuid4())

    def main1(self, username, password):
        try:
            self.h = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id',
                'cache-control': 'max-age=0',
                'dpr': '1',
                'priority': 'u=0, i',
                'referer': 'https://www.instagram.com/',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                'viewport-width': '673',
                'cookie': self.cokie['cookie']
            }
            self.r = requests.get('https://accountscenter.instagram.com/accounts/', headers=self.h).text
            self.u = re.findall('"multi_web_auth":\\[\\{"config":{"url":"(.*?)"',self.r)
            if self.u:
                self.url = self.u[0]
                self.url1 = self.url.replace('\\','')
                self.csrf = re.findall('csrftoken=(.*?);',str(self.cokie['cookie']))[0]
                self.etoken = re.findall('etoken=(.*?)&',self.url1)[0]
                self.hmac = re.search('"claim":"(.*?)"',self.r).group(1)
                self.head1 = {
                    'accept': '*/*',
                    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': self.cokie['cookie'],
                    'origin': 'https://www.instagram.com',
                    'priority': 'u=1, i',
                    'referer':self.url1,
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-ch-ua-platform-version': '"15.0.0"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                    'x-asbd-id': '129477',
                    'x-csrftoken': self.csrf,
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': self.hmac,
                    'x-instagram-ajax': '1019280819',
                    'x-requested-with': 'XMLHttpRequest',
                    'x-web-session-id': 'sjqmtd:wsfcpq:gwkev8',
                }
                self.data3 = {
                    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}',
                    'etoken': self.etoken,
                    'username': username
                }

                self.resp1 = requests.post('https://www.instagram.com/api/v1/web/fxcal/auth/login/ajax/',data=self.data3, headers=self.head1)
                if 'authenticated":true' in self.resp1.text:
                    print(f'[+] Login ke {self.data3['username']} berhasil')
                    self.head2 = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'id',
                        'cookie': self.cokie['cookie'],
                        'dpr': '1',
                        'priority': 'u=0, i',
                        'referer': 'https://www.instagram.com/',
                        'sec-ch-prefers-color-scheme': 'dark',
                        'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                        'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-model': '""',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-ch-ua-platform-version': '"15.0.0"',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'same-site',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                        'viewport-width': '673',
                    }
                    self.params = {
                        'auth_flow': 'ig_linking',
                        'background_page': '/',
                        'blob': self.resp1.json()['blob'],
                        'token': self.resp1.json()['token']
                    }
                    self.resp2 = requests.get('https://accountscenter.instagram.com/add/', params=self.params,headers=self.head2)
                    self.flsd = re.search('"LSD",\[\],{"token":"(.*?)"',self.resp2.text).group(1)
                    self.aktorid = re.search('"actorID":"(\d+)"',self.resp2.text).group(1)
                    self.hsi = re.search('"hsi":"(\d+)"',self.resp2.text).group(1)
                    self.hastesession = re.search('"haste_session":"(.*?)"',self.resp2.text).group(1)
                    self.rev = re.search('{"rev":(\d+)}',self.resp2.text).group(1)
                    self.spinr = re.search('"__spin_r":(\d+)',self.resp2.text).group(1)
                    self.spint = re.search('"__spin_t":(\d+)',self.resp2.text).group(1)
                    self.dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',self.resp2.text).group(1)
                    self.jazo = re.search('jazoest=(\d+)',self.resp2.text).group(1)
                    self.sessitiveurl = re.search('{"sensitive_string_value":"(.*?)"}',self.resp2.text).group(1)
                    self.head3 = {
                        'accept': '*/*',
                        'accept-language': 'id',
                        'content-type': 'application/x-www-form-urlencoded',
                        'cookie': self.cokie['cookie'],
                        'origin': 'https://accountscenter.instagram.com',
                        'priority': 'u=1, i',
                        'referer': self.resp2.url,
                        'sec-ch-prefers-color-scheme': 'dark',
                        'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                        'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-model': '""',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-ch-ua-platform-version': '"15.0.0"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                        'x-asbd-id': '129477',
                        'x-fb-friendly-name': 'FXLinkingFlowDisclosuresRefetchQuery',
                        'x-fb-lsd': self.flsd,
                        'x-ig-app-id': '936619743392459',
                    }
                    self.data4 = {
                        'av': self.aktorid,
                        '__user': '0',
                        '__a': '1',
                        '__req': 'i',
                        '__hs': self.hastesession,
                        'dpr': '1',
                        '__ccg': 'GOOD',
                        '__rev': self.rev,
                        '__s': 'liwoo5:rxplen:w0epet',
                        '__hsi': self.hsi,
                        '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo19oe8hw2nVE4W099w8G1Dz81s8hwnU2lwv89k2C1Fwc60D82IzXwae4UaEW0Loco5G0zK1swa-0nK3qazo7u0zEiwaG1LwTwNw4mwr86C1nw4xxW1owLwHwGwbu',
                        '__csr': 'gz6hBMP5ulkLA4thavAaBmSKiFDr4lQDt9LSAyFb_C9aVdbFtamzaGmt35ybKQGFdKCtbrmpBCCKFuVqbHbRSgytqgSGWAF9p4QbV-qmEWitKWmmiV4iJryFJbXGQbQ8niAHBzudyHQ5vAKl4hd3USuUkABCqyXh4iexi00k3WHwOg1to1vKFbGFfAxmGHwPKXCBK0Zo1zh7Bk8wEGhw15-URaEnjjg0OFaGGaGitdalauGwbiE0AO0lAx4bghJ399e1mIK2qt2FEbo332yCIS4IE94Ex7Gp1qq260nGAU4q4ohyE2ugK0rm9qvEs68J4wBga89VFrAAykVEIUyjKqZunK5omLEHwFCKE4uawa5ouxe8www19F6Dw',
                        '__comet_req': '24',
                        'fb_dtsg': self.dtsg,
                        'jazoest': self.jazo,
                        'lsd': self.flsd,
                        '__spin_r': self.spinr,
                        '__spin_b': 'trunk',
                        '__spin_t': self.spint,
                        'fb_api_caller_class': 'RelayModern',
                        'fb_api_req_friendly_name': 'FXLinkingFlowDisclosuresRefetchQuery',
                        'variables': '{"device_id":"device_id_fetch_ig_did","flow":"IG_WEB_SETTINGS","selected_age":27,"used_native_auth_in_vr":false,"web_auth":{"account_type":"INSTAGRAM","completion_url":{"sensitive_string_value":"'+self.sessitiveurl.replace('\\','')+'"},"web_auth_plain_token":{"sensitive_string_value":"USER_TOKEN"}}}',
                        'server_timestamps': 'true',
                        'doc_id': '9679270575423521',
                    }
                    self.resp3 = requests.post('https://accountscenter.instagram.com/api/graphql/',data=self.data4, headers=self.head3).text
                    try:self.opaque_target = re.search('"opaque_target_account_string":"(.*?)"',self.resp2.text).group(1)
                    except:
                        exit('\n[!] Akun ini sudah tidak bisa menambahkan, ganti tumbal')
                    self.data4.update({
                        'fb_api_req_friendly_name': 'useFXLinkMutation',
                        'variables': '{"client_mutation_id":"'+self.client+'","flow":"IG_WEB_SETTINGS","target_account_id":null,"target_account_type":"INSTAGRAM","target_auth_proof_string":{"sensitive_string_value":""},"device_id":"device_id_fetch_ig_did","interface":"IG_WEB","platform":"INSTAGRAM","scale":1,"selected_age_account_id":null,"selected_age_account_type":"INSTAGRAM","opaque_target_account_string":{"sensitive_string_value":"'+self.opaque_target+'"},"selected_opaque_age_account_id":{"sensitive_string_value":"Af7rQUAtikbs54Ugr2gtMydMmtUmPNvBoiTVc7JICKbmMj5JyoAN68G3PgE5rrE8lYiS6q6jVaW5X6U"},"show_age_updated_dialog":false,"used_native_auth_in_vr":false,"entrypoint":null,"reconciled_birthday":null,"reconciled_2fa_phone_number":null,"selected_supervision_account_id":null}',
                        'doc_id': '8717731548311624',
                    })
                    self.head3.update({'x-fb-friendly-name': 'useFXLinkMutation'})
                    self.resp4 = requests.post('https://accountscenter.instagram.com/api/graphql/',data=self.data4,headers=self.head3).text
                    if 'is_success":true' in self.resp4:
                        print(f'[+] akun {username} berhasil di tambahkan')
                    else:
                        print('[+] UPS eror ')
                elif 'checkpoint_required' in self.resp1.text:
                    print('\n[!] Login checkpoint')
                else:
                    print(f'\n[!] Login ke {username} gagal cek notifikasi atau coba ganti sandi')

            else:
                print('\n[!] Url Login tidak tersedia cek cokie tumbal')
        except Exception as e:
            print('[+] UPS eror ',e)
    
    def aktifkan2fa(self, data):
        try:
            self.head5 = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id',
                'cache-control': 'max-age=0',
                'cookie': self.cokie['cookie'],
                'dpr': '1',
                'priority': 'u=0, i',
                'referer': 'https://www.instagram.com/',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                'viewport-width': '673',
            }
            self.resp5 = requests.get('https://accountscenter.instagram.com/password_and_security/two_factor/',headers=self.head5).text
            self.akunList = re.findall('{"__typename":"XFBFXIGAccountInfo","id":"(\d+)","display_name":"(.*?)","platform_info":{"type":"INSTAGRAM","name":"Instagram"}',self.resp5)
            print(f'\n[+] Terdapat {len(self.akunList)} akun instagram\n')
            self.loop = 0
            for idakun,namaakun in self.akunList:
                self.loop+=1
                print(f'[{self.loop}]. {idakun}|{namaakun}')
            self.idakun = input('[?] Masukan id akun yang mau di aktifkan a2fnya : ')
            data.update({
                'fb_api_req_friendly_name': 'useFXSettingsTwoFactorGenerateTOTPKeyMutation',
                'variables': '{"input":{"client_mutation_id":"'+self.client+'","actor_id":"'+data['av']+'","account_id":"'+self.idakun+'","account_type":"INSTAGRAM","device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}',
                'doc_id': '6282672078501565',
            })
            self.head5.update({'x-fb-friendly-name': 'useFXSettingsTwoFactorGenerateTOTPKeyMutation',})
            self.resp6 = requests.post('https://accountscenter.instagram.com/api/graphql/',headers=self.head5, data=data)
            self.keys2 = re.search('"key_text":"(.*?)"',self.resp6.text).group(1)
            self.head_2f = {
                'accept': '*/*',
                'accept-language': 'id',
                'cookie': '_gcl_au=1.1.1496091412.1736620780; _ga=GA1.1.857719576.1736620782; _ga_R2SB88WPTD=GS1.1.1736620781.1.1.1736620796.0.0.0',
                'priority': 'u=1, i',
                'referer': 'https://2fa.live/',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                'x-requested-with': 'XMLHttpRequest',
            }
            self.token_2fa = requests.get(f'https://2fa.live/tok/{self.keys2.replace(" ","")}').json()['token']
            data.update({
                'fb_api_req_friendly_name': 'useFXSettingsTwoFactorEnableTOTPMutation',
                'variables': '{"input":{"client_mutation_id":"'+self.client+'","actor_id":"'+data['av']+'","account_id":"'+self.idakun+'","account_type":"INSTAGRAM","verification_code":"'+self.token_2fa+'","device_id":"device_id_fetch_ig_did","fdid":"device_id_fetch_ig_did"}}',
                'doc_id': '7032881846733167',
            })
            self.head5.update({'x-fb-friendly-name': 'useFXSettingsTwoFactorEnableTOTPMutation'})
            self.resp7 = requests.post('https://accountscenter.instagram.com/api/graphql/',headers=self.head5, data=data).text
            if 'success":true' in self.resp7:
                print(f'\n[+] Sukses 2FA Instagram\n[+] Secret Key : {self.keys2}\n')
                data.update({
                    'qpl_active_flow_ids': '433922143',
                    'fb_api_caller_class': 'RelayModern',
                    'fb_api_req_friendly_name': 'useFXSettingsTwoFactorFetchRecoveryCodesMutation',
                    'variables': '{"input":{"client_mutation_id":"'+self.client+'","actor_id":"'+data['av']+'","account_id":"'+self.idakun+'","account_type":"INSTAGRAM","fdid":"device_id_fetch_ig_did"}}',
                    'doc_id': '24140213678960162',
                    'fb_api_analytics_tags': '["qpl_active_flow_ids=433922143"]',
                })
                self.head5.update({'x-fb-friendly-name': 'useFXSettingsTwoFactorFetchRecoveryCodesMutation'})
                self.resp8 = requests.post('https://accountscenter.instagram.com/api/graphql/',headers=self.head5, data=data).text
                try:
                    self.kode_pemulihan = re.findall('"recovery_codes":(.*?)}',self.resp8)
                    for self.dihi in json.loads(self.kode_pemulihan[0]):
                        print(self.dihi)
                except Exception as e:print(e)
            else:
                print('\n[!] Terjadi kesalahan')
        except Exception as e:
            print('\n[!] Terjadi kesalahan ',e)
            exit()

    def GetContactPoint(self):
        try:
            self.head6 = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                'cache-control': 'max-age=0',
                'cookie': self.cokie['cookie'],
                'dpr': '1',
                'priority': 'u=0, i',
                'referer': 'https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=phone_number&contact_point_value=%2B6285366936081&dialog_type=contact_detail',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                'viewport-width': '673',
            }
            self.resp2 = requests.get('https://accountscenter.instagram.com/personal_info/contact_points/',headers=self.head6)
            self.contactList = re.findall('"normalized_contact_point":"(.*?)"',self.resp2.text)
            self.loop1 = 0
            print(f'\n[+] terdapat {len(self.contactList)} data\n')
            for self.kham in self.contactList:
                self.loop1+=1
                print(f'[{self.loop1}] {str(self.kham.replace("\\u0040","@"))}')
            self.remove_kontak = input('[?] Masukan Nomor/Email Jangan hapus +62 jika nomor : ')
            self.flsd = re.search('"LSD",\[\],{"token":"(.*?)"',self.resp2.text).group(1)
            self.aktorid = re.search('"actorID":"(\d+)"',self.resp2.text).group(1)
            self.hsi = re.search('"hsi":"(\d+)"',self.resp2.text).group(1)
            self.hastesession = re.search('"haste_session":"(.*?)"',self.resp2.text).group(1)
            self.rev = re.search('{"rev":(\d+)}',self.resp2.text).group(1)
            self.spinr = re.search('"__spin_r":(\d+)',self.resp2.text).group(1)
            self.spint = re.search('"__spin_t":(\d+)',self.resp2.text).group(1)
            self.dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',self.resp2.text).group(1)
            self.jazo = re.search('jazoest=(\d+)',self.resp2.text).group(1)
            self.asuidnendi = []
            try:
                self.targetid = re.search('"linked_accounts_from_contact_point":\[\{"__typename":"XFBFXIGAccountInfo","id":"(\d+)"}',self.resp2.text).group(1)
                self.asuidnendi.append(self.targetid)
            except:
                self.targetid = re.findall('{"__typename":"XFBFXIGAccountInfo","id":"(\d+)"',self.resp2.text)
                for memek in self.targetid:
                    if memek == self.aktorid:pass
                    else:self.asuidnendi.append(memek)
            self.targetid = self.asuidnendi[0]
            self.data5 = {
                'av': self.aktorid,
                '__user': '0',
                '__a': '1',
                '__req': 'i',
                '__hs': self.hastesession,
                'dpr': '1',
                '__ccg': 'GOOD',
                '__rev': self.rev,
                '__s': 'liwoo5:rxplen:w0epet',
                '__hsi': self.hsi,
                '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo19oe8hw2nVE4W099w8G1Dz81s8hwnU2lwv89k2C1Fwc60D82IzXwae4UaEW0Loco5G0zK1swa-0nK3qazo7u0zEiwaG1LwTwNw4mwr86C1nw4xxW1owLwHwGwbu',
                '__csr': 'gz6hBMP5ulkLA4thavAaBmSKiFDr4lQDt9LSAyFb_C9aVdbFtamzaGmt35ybKQGFdKCtbrmpBCCKFuVqbHbRSgytqgSGWAF9p4QbV-qmEWitKWmmiV4iJryFJbXGQbQ8niAHBzudyHQ5vAKl4hd3USuUkABCqyXh4iexi00k3WHwOg1to1vKFbGFfAxmGHwPKXCBK0Zo1zh7Bk8wEGhw15-URaEnjjg0OFaGGaGitdalauGwbiE0AO0lAx4bghJ399e1mIK2qt2FEbo332yCIS4IE94Ex7Gp1qq260nGAU4q4ohyE2ugK0rm9qvEs68J4wBga89VFrAAykVEIUyjKqZunK5omLEHwFCKE4uawa5ouxe8www19F6Dw',
                '__comet_req': '24',
                'fb_dtsg': self.dtsg,
                'jazoest': self.jazo,
                'lsd': self.flsd,
                '__spin_r': self.spinr,
                '__spin_b': 'trunk',
                '__spin_t': self.spint,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'FXAccountsCenterDeleteContactPointMutation',
                'variables': '{"normalized_contact_point":"'+self.remove_kontak+'","contact_point_type":"PHONE_NUMBER","selected_accounts":["'+self.targetid+'"],"client_mutation_id":"mutation_id_1736662886463","family_device_id":"device_id_fetch_ig_did"}' if '@' not in self.remove_kontak else '{"normalized_contact_point":"'+self.remove_kontak+'","contact_point_type":"EMAIL","selected_accounts":["'+self.targetid+'"],"client_mutation_id":"mutation_id_1736664078315","family_device_id":"device_id_fetch_ig_did"}',
                'server_timestamps': 'true',
                'doc_id': '6716611361758391',
            }
            self.head7 = {
                'accept': '*/*',
                'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': self.cokie['cookie'],
                'origin': 'https://accountscenter.instagram.com',
                'priority': 'u=1, i',
                'referer': 'https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=phone_number&contact_point_value=%2B6285366936081&dialog_type=contact_detail',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                'x-asbd-id': '129477',
                'x-fb-friendly-name': 'FXAccountsCenterDeleteContactPointMutation',
                'x-fb-lsd': self.flsd,
                'x-ig-app-id': '936619743392459',
            }
            self.resp9 = requests.post('https://accountscenter.instagram.com/api/graphql/',data=self.data5,headers=self.head7).text
            if 'reauth_accounts' in self.resp9:
                print('\n[!] Shit boy, Login ulang, masukan data akun yang mau di a2f')
                username = input('[?] Username : ')
                password = input('[?] Password : ')
                self.profile = re.search('"profile_identifier":"(.*?)"',self.resp9).group(1)
                self.head7.update({ 'x-fb-friendly-name': 'FXReauthDialogPageQuery',})
                self.data5.update({
                    'fb_api_req_friendly_name': 'FXReauthDialogPageQuery',
                    'variables': '{"account_type":"INSTAGRAM","device_id":"device_id_fetch_ig_did","extra_data":"/personal_info/contact_points/?contact_point_type=email&contact_point_value='+self.remove_kontak+'&dialog_type=contact_detail","force_logout":false,"node_id":"CONTACT_POINT","reauth_initiator_flow":"SETTINGS","target_userid":"'+self.profile+'","use_fxcal_reauth_cadam":true,"include_reauth":true,"single_reauth":true,"interface":"IG_WEB"}',
                    'doc_id': '8882706878428466',
                })
                self.resp10 = requests.post('https://accountscenter.instagram.com/api/graphql/',data=self.data5,headers=self.head7).text
                self.curlfc = re.search('"web_auth":{"url":"(.*?)"',self.resp10).group(1)
                self.csrf = re.findall('csrftoken=(.*?);',str(self.cokie['cookie']))[0]
                self.etoken = re.findall('etoken=(.*?)&',self.curlfc)[0]
                self.head8 = {
                    'accept': '*/*',
                    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': self.cokie['cookie'],
                    'origin': 'https://www.instagram.com',
                    'priority': 'u=1, i',
                    'referer': self.curlfc,
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-ch-ua-platform-version': '"15.0.0"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                    'x-asbd-id': '129477',
                    'x-csrftoken': self.csrf,
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': 'hmac.AR2_xDloXEXYIJSwM7CbzgKcufxMrGEleattMT8eYoTbcMeK',
                    'x-instagram-ajax': '1019280819',
                    'x-requested-with': 'XMLHttpRequest',
                    'x-web-session-id': 'f3er7u:kzozjw:90bibv',
                }
                self.data6 = {
                    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}',
                    'etoken': self.etoken,
                    'username': username
                }
                self.resp11 = requests.post('https://www.instagram.com/api/v1/web/fxcal/auth/login/ajax/',data=self.data6,headers=self.head8)
                if 'authenticated":true' in self.resp11.text:
                    self.params = {
                        'contact_point_type': 'email',
                        'contact_point_value': self.remove_kontak,
                        'dialog_type': 'contact_detail',
                        'auth_flow': 'reauth',
                        'blob': self.resp11.json()['blob'],
                        'token': self.resp11.json()['token']
                    }
                    self.head9 = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                        'cookie': self.cokie['cookie'],
                        'dpr': '1',
                        'priority': 'u=0, i',
                        'referer': 'https://www.instagram.com/',
                        'sec-ch-prefers-color-scheme': 'dark',
                        'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                        'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-model': '""',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-ch-ua-platform-version': '"15.0.0"',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'same-site',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                        'viewport-width': '673',
                    }
                    self.resp12 = requests.get('https://accountscenter.instagram.com/personal_info/contact_points/',params=self.params, headers=self.head9).text
                    print('\n[+] Berhasil Login, coba jalankan ulang\n')
                    self.GetContactPoint()
                else:
                    print('[!] Gagal Login :(')
            elif '"api_error_code":200' in self.resp9:
                print('\n[!] Di suruh masukin password bang aduh')
                self.ipas = input('[?] Masukan password akun yang mau di hapus data : ')
                self.pasw = f"#PWD_BROWSER:0:{int(time.time())}:{self.ipas}"
                self.data5.update({
                    'fb_api_req_friendly_name': 'FXPasswordReauthenticationMutation',
                    'variables': '{"input":{"account_id":"'+self.targetid+'","account_type":"INSTAGRAM","category_name":"SecuredActionDeleteMetaContactPointCategory","password":{"sensitive_string_value":"'+self.pasw+'"},"actor_id":"'+self.data5['av']+'","client_mutation_id":"1"}}',
                    'server_timestamps': 'true',
                    'doc_id': '5864546173675027',
                })
                self.head7.update({'x-fb-friendly-name': 'FXPasswordReauthenticationMutation'})
                self.resp392 = requests.post('https://accountscenter.instagram.com/api/graphql/',data=self.data5, headers=self.head7).text
                if 'success":true' in self.resp392:
                    print('\n[+] Berhasil Reauth, ulangi langkah tadi\n')
                    self.GetContactPoint()
                else:
                    exit('\n[!] gagal reauth')
            elif 'success":false' in self.resp9:
                print(f'[+] Gagal hapus {self.remove_kontak}, coba tambah email/nomor terlebih dahulu')
            elif 'success":true' in self.resp9:
                print(f'[+] Kontak {self.remove_kontak} berhasil di hapus')
            else:
                print('[!] Mohon maaf ada respon yang tidak di ketahui')
        except Exception as e:
            print('\n[!] Terjadi kesalahan ',e)
    
    def Getkode(self, email):
        self.kodec = []
        while True:
            try:
                self.memeks = {
                    'sec-ch-ua-platform': '"Windows"',
                    'Referer': f'https://inboxkitten.com/inbox/{email}/list',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                    'Accept': 'application/json, text/plain, */*',
                    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                }
                self.resp203 = requests.get(f'https://inboxkitten.com/api/v1/mail/list?recipient={email}', headers=self.memeks).text
                self.sdcards = re.findall('"storage":{"key":"(.*?)","region":"(.*?)"',self.resp203)
                self.head20 = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                    'priority': 'u=0, i',
                    'referer': f'https://inboxkitten.com/',
                    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'iframe',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                }
                self.params2 = {'region': self.sdcards[0][1],'key': self.sdcards[0][0].split('"')[0],}
                self.resp332 = parser(requests.get('https://inboxkitten.com/api/v1/mail/getHtml',params=self.params2,headers=self.head20).text,'html.parser')
                for self.xyzu in self.resp332.find_all('td'):
                    self.kode = re.findall('Anda mungkin diminta untuk memasukkan kode konfirmasi ini:(\d+)',self.xyzu.text)
                    if self.kode: self.kodec.append(self.kode[0])
                break
            except:continue
        return self.kodec[0]

    def AddEmail(self, gmail):
        try:
            if gmail == None:email = ''.join(random.choice(string.ascii_lowercase+string.digits) for x in range(random.randint(5,10))) + '@inboxkitten.com'
            else:email = gmail
            self.head33 = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                'cache-control': 'max-age=0',
                'cookie': self.cokie['cookie'],
                'dpr': '1',
                'priority': 'u=0, i',
                'referer': 'https://accountscenter.instagram.com',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                'viewport-width': '1358',
            }
            self.resp2 = requests.get('https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point', headers=self.head33)
            self.akunList = re.findall('"id":"(.*?)","profile_identifier":"(.*?)","display_name":"(.*?)"',self.resp2.text)
            print('')
            self.loop2 = 0
            for a,b,c in self.akunList:
                self.loop2 +=1
                print(f'[{self.loop2}] {a}|{c}')
            
            self.targetID = input('\n[?] Masukan id akun di atas : ')
            self.flsd = re.search('"LSD",\[\],{"token":"(.*?)"',self.resp2.text).group(1)
            self.aktorid = re.search('"actorID":"(\d+)"',self.resp2.text).group(1)
            self.hsi = re.search('"hsi":"(\d+)"',self.resp2.text).group(1)
            self.hastesession = re.search('"haste_session":"(.*?)"',self.resp2.text).group(1)
            self.rev = re.search('{"rev":(\d+)}',self.resp2.text).group(1)
            self.spinr = re.search('"__spin_r":(\d+)',self.resp2.text).group(1)
            self.spint = re.search('"__spin_t":(\d+)',self.resp2.text).group(1)
            self.dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',self.resp2.text).group(1)
            self.jazo = re.search('jazoest=(\d+)',self.resp2.text).group(1)
            self.head10 = {
                'accept': '*/*',
                'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': self.cokie['cookie'],
                'origin': 'https://accountscenter.instagram.com',
                'priority': 'u=1, i',
                'referer': 'https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                'x-asbd-id': '129477',
                'x-fb-friendly-name': 'FXAccountsCenterAddContactPointMutation',
                'x-fb-lsd': self.flsd,
                'x-ig-app-id': '936619743392459',
            }
            self.data8 = {
                'av': self.aktorid,
                '__user': '0',
                '__a': '1',
                '__req': 'p',
                '__hs': self.hastesession,
                'dpr': '1',
                '__ccg': 'GOOD',
                '__rev': self.rev,
                '__s': '63p87z:jm9uhf:5ogubp',
                '__hsi': self.hsi,
                '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo19oe8hw2nVE4W099w8G1Dz81s8hwnU2lwv89k2C1Fwc60D82IzXwae4UaEW0Loco5G0zK1swa-0nK3qazo7u0zEiwaG1LwTwNw4mwr86C1nw4xxW1owLwHwGwbu',
                '__csr': 'gJMB7NJnZWERRRtp5mCyH_49kCh9ZQ_TIJpGEJH9b_JqEGfVTllAUEF9GJpXJvAA8ABADiD8IFpkZaWhVZ_h4rFXsRtqKrRQ9CAABCmbATmXvpTGvVoWeWxpGhagNVe4UDmWADHiBBDAyEy9QECWyFoymiaGFFQ9DF16-00k7B2WyK3p0oE2qyHw6iwk8CHBGFe5fGmE1WJwaa1024x1w0uUG3mdigK8iGp2biiw2xFpVEgzXJdd0kXjAhQ5bggLU1ObUfUaU2lCkwrppUkxmAXCDG0puq22AU0CzFHNU2Zg8GxC2mi6aYNUOub8ECpzFhm3yWzbG1gwmGGEl-E-jmUf80j3oS',
                '__comet_req': '24',
                'fb_dtsg': self.dtsg,
                'jazoest': self.jazo,
                'lsd': self.flsd,
                '__spin_r': self.spinr,
                '__spin_b': 'trunk',
                '__spin_t': self.spint,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'FXAccountsCenterAddContactPointMutation',
                'variables': '{"country":"ID","contact_point":"'+email+'","contact_point_type":"email","selected_accounts":["'+self.targetID+'"],"family_device_id":"device_id_fetch_ig_did","client_mutation_id":"mutation_id_1736685144850"}',
                'server_timestamps': 'true',
                'doc_id': '6970150443042883'
            }
            self.resp13 = requests.post('https://accountscenter.instagram.com/api/graphql/',headers=self.head10,data=self.data8).text
            if 'success":true' in self.resp13:
                if gmail == None:self.kode = self.Getkode(email)
                else:self.kode = input('[?] Masukan kode yang di kirim ke email : ')
                self.head10.update({ 'x-fb-friendly-name': 'FXAccountsCenterContactPointConfirmationDialogVerifyContactPointMutation',})
                self.data8.update({
                    'fb_api_req_friendly_name': 'FXAccountsCenterContactPointConfirmationDialogVerifyContactPointMutation',
                    'variables': '{"contact_point":"'+email+'","contact_point_type":"email","pin_code":"'+self.kode+'","selected_accounts":["'+self.targetID+'"],"family_device_id":"device_id_fetch_ig_did","client_mutation_id":"mutation_id_1736685196293","contact_point_event_type":"ADD","normalized_contact_point_to_replace":""}',
                    'doc_id': '8108292719198518',
                })
                self.resp14 = requests.post('https://accountscenter.instagram.com/api/graphql/',headers=self.head10,data=self.data8).text
                if 'success":true' in self.resp14:
                    print(f'\n[+] Berhasil tambahkan email {email}')
                else:
                    print(f'\n[+] Gagal tambahkan email {email}')
            else:
                print(f'\n[+] Gagal tambahkan email {email}')
        except Exception as e:
            print('\n[!] Terjadi kesalahan ',e)

    def GetListAkunAndRemove(self):
        try:
            self.head304 = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                'cache-control': 'max-age=0',
                'cookie': self.cokie['cookie'],
                'dpr': '1',
                'priority': 'u=0, i',
                'referer': 'https://www.instagram.com/',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                'viewport-width': '673',
            }
            self.resp404 = requests.get('https://accountscenter.instagram.com/accounts/',headers=self.head304)
            self.akunList = re.findall('"id":"fxim:identity:(\d+)"',self.resp404.text)
            self.flsd = re.search('"LSD",\[\],{"token":"(.*?)"',self.resp404.text).group(1)
            self.aktorid = re.search('"actorID":"(\d+)"',self.resp404.text).group(1)
            self.hsi = re.search('"hsi":"(\d+)"',self.resp404.text).group(1)
            self.hastesession = re.search('"haste_session":"(.*?)"',self.resp404.text).group(1)
            self.rev = re.search('{"rev":(\d+)}',self.resp404.text).group(1)
            self.spinr = re.search('"__spin_r":(\d+)',self.resp404.text).group(1)
            self.spint = re.search('"__spin_t":(\d+)',self.resp404.text).group(1)
            self.dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',self.resp404.text).group(1)
            self.jazo = re.search('jazoest=(\d+)',self.resp404.text).group(1)
            print('')
            self.loop3 = 0
            for self.uih in self.akunList:
                self.loop3 +=1
                print(f'[{self.loop3}] {self.uih}')
            self.akuns = input('\n[?] Hapus akun Facebook/instagram [fb/ig] : ').lower()
            if self.akuns == 'fb':
                self.uid_remove = input('\n[?] Masukan id fbnya : ')
                self.datafb = {
                    'av': self.aktorid,
                    '__user': '0',
                    '__a': '1',
                    '__req': 's',
                    '__hs': self.hastesession,
                    'dpr': '1',
                    '__ccg': 'GOOD',
                    '__rev': self.rev,
                    '__s': '4eze2i:ovkjiy:gpo309',
                    '__hsi': self.hsi,
                    '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo19oe8hw2nVE4W099w8G1Dz81s8hwnU2lwv89k2C1Fwc60D82IzXwae4UaEW0Loco5G0zK1swa-0nK3qazo7u0zEiwaG1LwTwNw4mwr86C1nw4xxW1owLwHwGwbu',
                    '__csr': 'gFd7jgHPQ_viQLOYBKDiRF8BIGlqlELVAKAnJbfnibZfB49kiBSRqKAAimyequpkTGHgOBAGl9e8rznZjAGWB99iJp4zqGBXKAtrVFLCGiVvVuEFuRy9ebCGjOGh4RlGE-m5oGA-4eLy5hVpu7GBymKmF8hG4KEWchWw0573xSiWHGVE551m0K8nK2t0Qw6mGuGHGbxmi0vvEAWx51b2o4Aw2Cw18qAV4i2u2u48iiw2BoGqha2CcG6ri-GDmWw3cA2KLylhk0KXK0Skq2dd5wmEaokjg6uaDgGJxulQ3h1SE1kA1nw2wkAwC0LQ3q2mF8vEx9t5BKH4PGpape3q6pECXy84u1vGAmUgQ6eiGwNw12Yw',
                    '__comet_req': '24',
                    'fb_dtsg': self.dtsg,
                    'jazoest': self.jazo,
                    'lsd': self.flsd,
                    '__spin_r': self.spinr,
                    '__spin_b': 'trunk',
                    '__spin_t': self.spint,
                    'fb_api_caller_class': 'RelayModern',
                    'fb_api_req_friendly_name': 'useFXUnlinkMutation',
                    'variables': '{"client_mutation_id":"'+str(uuid.uuid4())+'","account_id":"'+self.uid_remove+'","account_type":"FACEBOOK","flow":"IG_WEB_SETTINGS","device_id":"device_id_fetch_ig_did","interface":"IG_WEB","platform":"INSTAGRAM","scale":1,"entrypoint":null}',
                    'server_timestamps': 'true',
                    'doc_id': '7842315685871396',
                }
                self.headfb = {
                    'accept': '*/*',
                    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': self.cokie['cookie'],
                    'origin': 'https://accountscenter.instagram.com',
                    'priority': 'u=1, i',
                    'referer': 'https://accountscenter.instagram.com/accounts/?theme=dark',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.146", "Chromium";v="131.0.6778.265", "Not_A Brand";v="24.0.0.0"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-ch-ua-platform-version': '"15.0.0"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                    'x-asbd-id': '129477',
                    'x-fb-friendly-name': 'useFXUnlinkMutation',
                    'x-fb-lsd': self.flsd,
                    'x-ig-app-id': '936619743392459',
                }
                self.removefb = requests.post('https://accountscenter.instagram.com/api/graphql/',data=self.datafb,headers=self.headfb).text
                if 'Anda menghapus ' in self.removefb:
                    print(f'[+] Akun facebook {self.uid_remove} di hapus dari ig')
                else:
                    print(f'[+] Akun facebook {self.uid_remove} gagal di hapus')
            else:
                self.uid_remove = input('\n[?] Masukan id ignya : ')
                self.dataig = {
                    'av': self.aktorid,
                    '__user': '0',
                    '__a': '1',
                    '__req': 's',
                    '__hs': self.hastesession,
                    'dpr': '1',
                    '__ccg': 'GOOD',
                    '__rev': self.rev,
                    '__s': '4eze2i:ovkjiy:gpo309',
                    '__hsi': self.hsi,
                    '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo19oe8hw2nVE4W099w8G1Dz81s8hwnU2lwv89k2C1Fwc60D82IzXwae4UaEW0Loco5G0zK1swa-0nK3qazo7u0zEiwaG1LwTwNw4mwr86C1nw4xxW1owLwHwGwbu',
                    '__csr': 'gFd7jgHPQ_viQLOYBKDiRF8BIGlqlELVAKAnJbfnibZfB49kiBSRqKAAimyequpkTGHgOBAGl9e8rznZjAGWB99iJp4zqGBXKAtrVFLCGiVvVuEFuRy9ebCGjOGh4RlGE-m5oGA-4eLy5hVpu7GBymKmF8hG4KEWchWw0573xSiWHGVE551m0K8nK2t0Qw6mGuGHGbxmi0vvEAWx51b2o4Aw2Cw18qAV4i2u2u48iiw2BoGqha2CcG6ri-GDmWw3cA2KLylhk0KXK0Skq2dd5wmEaokjg6uaDgGJxulQ3h1SE1kA1nw2wkAwC0LQ3q2mF8vEx9t5BKH4PGpape3q6pECXy84u1vGAmUgQ6eiGwNw12Yw',
                    '__comet_req': '24',
                    'fb_dtsg': self.dtsg,
                    'jazoest': self.jazo,
                    'lsd': self.flsd,
                    '__spin_r': self.spinr,
                    '__spin_b': 'trunk',
                    '__spin_t': self.spint,
                    'fb_api_caller_class': 'RelayModern',
                    'fb_api_req_friendly_name': 'useFXUnlinkMutation',
                    'variables': '{"client_mutation_id":"'+str(uuid.uuid4())+'","account_id":"'+self.uid_remove+'","account_type":"INSTAGRAM","flow":"IG_WEB_SETTINGS","device_id":"device_id_fetch_ig_did","interface":"IG_WEB","platform":"INSTAGRAM","scale":1,"entrypoint":null}',
                    'server_timestamps': 'true',
                    'doc_id': '7842315685871396',
                }
                self.headig = {
                    'accept': '*/*',
                    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': self.cokie['cookie'],
                    'origin': 'https://accountscenter.instagram.com',
                    'priority': 'u=1, i',
                    'referer': 'https://accountscenter.instagram.com/accounts/',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.146", "Chromium";v="131.0.6778.265", "Not_A Brand";v="24.0.0.0"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-ch-ua-platform-version': '"15.0.0"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                    'x-asbd-id': '129477',
                    'x-fb-friendly-name': 'useFXUnlinkMutation',
                    'x-fb-lsd': self.flsd,
                    'x-ig-app-id': '936619743392459',
                }
                self.removeig = requests.post('https://accountscenter.instagram.com/api/graphql/', data=self.dataig,headers=self.headig)
                if 'Anda menghapus ' in self.removeig:
                    print(f'[+] Akun instagram {self.uid_remove} di hapus')
                else:
                    print(f'[+] Akun instagram {self.uid_remove} gagal di hapus')

        except Exception as e:
            print('\n[!] Terjadi kesalahan ',e)

class menuUser:
    def __init__(self):
        pass

    def infoUser(self, cookies):
        try:
            InfoHeaders = {'x-ig-app-locale': 'in_ID','x-ig-device-locale': 'in_ID','x-ig-mapped-locale': 'id_ID','x-bloks-version-id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb','x-bloks-is-layout-rtl': 'false','x-ig-capabilities': '3brTv10=','x-ig-app-id': '567067343352427','priority': 'u=3','user-agent': 'Instagram 275.0.0.27.98 Android (25/7.1.2; 240dpi; 720x1280; Google/google; google Pixel 2; x86; android_x86; in_ID; 458229257)','accept-language': 'id-ID, en-US','x-fb-http-engine': 'Liger','x-fb-client-ip': 'True','x-fb-server-cluster': 'True'}
            self.user = re.search('ds_user_id=(\d+)',str(cookies)).group(1)
            self.info = requests.get(f'https://i.instagram.com/api/v1/users/{self.user}/info/', headers=InfoHeaders, cookies = {'cookie':cookies}).json()['user']
            self.namanme = self.info['full_name']
            self.followers = self.info['follower_count']
            self.following = self.info['following_count']
            open('tumbal','w').write(cookies)
            print(f'[+] Tumbal 2FA {self.namanme} -> {self.followers}/{self.following}')
        except Exception:
            print('[+] Tumbal kamu invalid')
            cokie = input('[?] Masukan cokie tumbal : ')
            os.system('clear')
            self.infoUser(cokie)

    def GetListAkun(self, cokie):
        try:
            self.head1 = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                'cache-control': 'max-age=0',
                'cookie': cokie,
                'dpr': '1',
                'priority': 'u=0, i',
                'referer': 'https://web.facebook.com/',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                'viewport-width': '1358',
            }
            self.resp1 = requests.get('https://accountscenter.instagram.com/accounts/', headers=self.head1).text
            self.namae = list(set(re.findall('"display_name":"(.*?)"',self.resp1)))
            return self.namae
        except:return []

    def menu(self):
        os.system('clear')
        print('[+] Automation instagram 2FA')
        print(f'[+] Licensi kamu tersisa {D}{validateUser().file_key()} {W}hari\n')
        if os.path.isfile('tumbal') == False:
            cokie = input('[?] Masukan cokie tumbal : ')
            self.infoUser(cokie)
        else:
            cokie = open('tumbal','r').read()
            akunterhubung = self.GetListAkun(cokie)
            self.infoUser(cokie)
            if len(akunterhubung) >=3:
                print(f'[{D}!{W}] Terlalu banyak akun {D}hapus terlebih dahulu{W}')
            print('\n[1] Tambahkan akun yang mau di 2FA')
            print('[2] Aktifkan 2FA instagram')
            print('[3] Hapus Nomor/Email dan tambah')
            print('[4] Hapus akun yang terhubung')
            print('[5] Baca Tutorial')
            print('[0] Logout\n')
            xyz = input('[?] Choose : ')
            if xyz == '1':
                print('\n[!] masukan data akun yang mau di tambahkan')
                username = input('[?] masukan username : ')
                password = input('[?] masukan password : ')
                print('\n[+] Tunggu proses beberapa detik-menit')
                login(cokie).main1(username,password)
                exit(1)
            elif xyz == '2':
                try:
                    self.head3 = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                        'cache-control': 'max-age=0',
                        'cookie': cokie,
                        'dpr': '1',
                        'priority': 'u=0, i',
                        'referer': 'https://accountscenter.instagram.com',
                        'sec-ch-prefers-color-scheme': 'dark',
                        'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                        'sec-ch-ua-full-version-list': '"Microsoft Edge";v="131.0.2903.112", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-model': '""',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-ch-ua-platform-version': '"15.0.0"',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
                        'viewport-width': '1358',
                    }
                    self.resp2 = requests.get('https://accountscenter.instagram.com/', headers=self.head3)
                    self.flsd = re.search('"LSD",\[\],{"token":"(.*?)"',self.resp2.text).group(1)
                    self.aktorid = re.search('"actorID":"(\d+)"',self.resp2.text).group(1)
                    self.hsi = re.search('"hsi":"(\d+)"',self.resp2.text).group(1)
                    self.hastesession = re.search('"haste_session":"(.*?)"',self.resp2.text).group(1)
                    self.rev = re.search('{"rev":(\d+)}',self.resp2.text).group(1)
                    self.spinr = re.search('"__spin_r":(\d+)',self.resp2.text).group(1)
                    self.spint = re.search('"__spin_t":(\d+)',self.resp2.text).group(1)
                    self.dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',self.resp2.text).group(1)
                    self.jazo = re.search('jazoest=(\d+)',self.resp2.text).group(1)
                    self.data40 = {
                        'av': self.aktorid,
                        '__user': '0',
                        '__a': '1',
                        '__req': 'i',
                        '__hs': self.hastesession,
                        'dpr': '1',
                        '__ccg': 'GOOD',
                        '__rev': self.rev,
                        '__s': 'liwoo5:rxplen:w0epet',
                        '__hsi': self.hsi,
                        '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo19oe8hw2nVE4W099w8G1Dz81s8hwnU2lwv89k2C1Fwc60D82IzXwae4UaEW0Loco5G0zK1swa-0nK3qazo7u0zEiwaG1LwTwNw4mwr86C1nw4xxW1owLwHwGwbu',
                        '__csr': 'gz6hBMP5ulkLA4thavAaBmSKiFDr4lQDt9LSAyFb_C9aVdbFtamzaGmt35ybKQGFdKCtbrmpBCCKFuVqbHbRSgytqgSGWAF9p4QbV-qmEWitKWmmiV4iJryFJbXGQbQ8niAHBzudyHQ5vAKl4hd3USuUkABCqyXh4iexi00k3WHwOg1to1vKFbGFfAxmGHwPKXCBK0Zo1zh7Bk8wEGhw15-URaEnjjg0OFaGGaGitdalauGwbiE0AO0lAx4bghJ399e1mIK2qt2FEbo332yCIS4IE94Ex7Gp1qq260nGAU4q4ohyE2ugK0rm9qvEs68J4wBga89VFrAAykVEIUyjKqZunK5omLEHwFCKE4uawa5ouxe8www19F6Dw',
                        '__comet_req': '24',
                        'fb_dtsg': self.dtsg,
                        'jazoest': self.jazo,
                        'lsd': self.flsd,
                        '__spin_r': self.spinr,
                        '__spin_b': 'trunk',
                        '__spin_t': self.spint,
                        'fb_api_caller_class': 'RelayModern',
                        'fb_api_req_friendly_name': 'FXLinkingFlowDisclosuresRefetchQuery',
                        'server_timestamps': 'true',
                        'doc_id': '9679270575423521',
                    }
                    login(cokie).aktifkan2fa(self.data40)
                except Exception as e:
                    print('\n[!] Terjadi kesalahan',e)

            elif xyz == '3':
                print(f'\n[1] Hapus email\n[2] Tambah email ({D}Email sebelumnnya akan terhapus{W})\n')
                dih = input('[?] Chose : ')
                if dih == '1':login(cokie).GetContactPoint()
                else:
                    print(f'\n[1] Random Email {D}Inboxkitten{W}\n[2] Email kamu sendiri\n')
                    self.chs = input('[?] Siapa ayo : ')
                    if self.chs == '2':self.email = input('\n[?] Masukan Emailmu : ')
                    else:self.email = None
                    login(cokie).AddEmail(self.email)
            elif xyz == '4':login(cokie).GetListAkunAndRemove()
            elif xyz == '5':
                print('\n[ Tutorial Sedernana ]')
                print('''
pertama kalian tambahkan akun yang mau di aktifin a2f nya
kalian pilih menu nomor satu, jika sudah berhasil di tambahkan
lanjut aktifin a2f, nomor 2 atau tambah email bebas 
syarat wajib akun tumbal belum terhubung ke akun manapun fb maupun ig.
                ''')
                self.tonton = input('[?] Lihat tutorial di YT [y/t]: ').lower()
                if self.tonton == 'y':os.system('xdg-open ')


def clear():
    os.system('clear' if 'linux' in sys.platform.lower() else 'cls')

class validateUser:
    def __init__(self):
        pass
    
    def file_key(self):
        if os.path.isfile('.kunci') == False:
            self.buy_key()
        else:
            self.keys = open('.kunci','r').read()
            self.sisa = self.durasi(self.keys)
            return(self.sisa)
    
    def cek_hash(self, xxx):
        try:
            self.rrq = requests.get('https://pastebin.com/raw/2hXEZff7').text
            self.key = re.findall(xxx+'.*',self.rrq)
            if len(self.key) > 0: return False
            else:return True
        except (requests.exceptions.ConnectionError,requests.RequestException):
            exit('\n[!] Cek koneksi kamu')

    def buy_key(self):
        clear()
        self.now = datetime.now()
        self.joined = '%s-%s-%s'%(self.now.day,self.now.month,self.now.year)
        self.random = str(uuid.uuid4()) + str(random.randint(1,99999)) + str(self.joined)
        self.hashing = hashlib.md5(self.random.encode()).hexdigest()
        self.valid =  self.cek_hash(self.hashing)
        if self.valid == True:
            open('.kunci','w').write(self.hashing)
            print(f'[+] License : {self.hashing}')
            print(f'[+] Kamu akan di arahkan ke whatsapp, tunggu ada respon author')
            os.system(f'xdg-open https://wa.me/+6283853140469?text={self.hashing}')
            exit()
        else:
            self.buy_key()
    
    def durasi(self,xxx):
        try:
            self.rrq = requests.get('https://pastebin.com/raw/2hXEZff7').text
            self.key = re.findall(xxx+'.*',self.rrq)[0].split('|')[1]
            hari,bulan,tahun = self.key.split('-')
            self.sisa = date(int(tahun),int(bulan),int(hari))
            self.ptim = datetime.strptime(str(self.sisa),"%Y-%m-%d")
            self.xtim = self.ptim.date() - date.today()
            if self.xtim.days <1:
                os.remove('.kunci')
                print(f'\n[!] license anda sudah habis, silahkan perpanjang, kode unik anda : {xxx}')
                exit()
            else:
                return self.xtim.days
        except IndexError:
            os.remove('.kunci')
            exit('[!] License salah')
        except Exception as e:
            exit(e)

def KONTOL3x():
    menuUser().menu()
