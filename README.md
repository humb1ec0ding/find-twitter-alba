# find-twitter-alba
find-twitter-alba

![](https://raw.githubusercontent.com/humb1ec0ding/humb1ec0ding-etc/master/2015/02/twitter-alba.png)

그들은 누굴까 ? 

Twitter **Python** Client 연습할 겸으로 API 몇 개 써보자... :)


## Requirement

* [Twitter Apps](https://apps.twitter.com/) 에서 Twitter client OAuth token 생성해야 함.
```python
# Create Twitter Apps : https://apps.twitter.com/
client = UserClient(CONSUMER_KEY,
                    CONSUMER_SECRET,
                    ACCESS_TOKEN,
                    ACCESS_TOKEN_SECRET)
```
* [birdy](https://github.com/inueni/birdy) is a super awesome Twitter API client for Python in just a little under 400 LOC.


## Starting point 

### [Feb,22] 프로필 사진, id, 이름, 계정 생성 시간

`2015.02.22` 확인 결과 동작하는 `twitter` 계정들.
![](http://pbs.twimg.com/profile_images/566790281496784897/RlS2Veg4_normal.jpeg)        ohademayochuchu 돌아온 미숙이   Thu Dec 04 05:57:22 +0000 2014 <br>
![](http://pbs.twimg.com/profile_images/2604817910/r_normal.jpg)        shinytart       이지영  Thu Sep 13 06:55:06 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2604826784/s_normal.jpg)        tiny_farm1      eunlin  Thu Sep 13 07:07:32 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2661693763/83859a1bf7d4a734615dc3483147e837_normal.jpeg)        bonussa01       지은현  Sat Sep 29 11:47:21 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2661713669/b6ef314f340f03dd97f5d34433b25ad2_normal.jpeg)        bonussa02       정지연  Sat Sep 29 11:52:27 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2661726096/841ac58975f8a35090620dbac0e41dac_normal.jpeg)        bonussa03       민      Sat Sep 29 12:00:22 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2661744181/a20bc0fcbad87f455749a9d267863d43_normal.jpeg)        bonussa04       이은정  Sat Sep 29 12:07:51 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2661756755/3a8433962f2e11bcccf5f6993ab10bc5_normal.jpeg)        bonussa05       이수진  Sat Sep 29 12:12:47 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2673595699/97556606b9429639a471b787ff5f2c3a_normal.jpeg)        kojisiktaxi01   김수진  Tue Oct 02 16:17:42 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2673615067/b6ef314f340f03dd97f5d34433b25ad2_normal.jpeg)        kojisiktaxi02   이연지  Tue Oct 02 16:24:54 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2682578123/547ac5a3c1dcd47f51925e47eafbda6d_normal.jpeg)        kojisiktaxi04   이지수  Fri Oct 05 07:48:28 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2673850215/841ac58975f8a35090620dbac0e41dac_normal.jpeg)        kojisiktaxi03   이지현  Tue Oct 02 17:47:29 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2690916682/2fab84ca7f19ae58280dfc485c37c01f_normal.jpeg)        sja_super01     Kim ji hyun     Sun Oct 07 15:21:32 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2690958834/138445ec4e40a8af10c0cc9ff61441b1_normal.jpeg)        sja_super02     이진수  Sun Oct 07 15:34:04 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2691000011/e7d5da52772c774756103060baaf0025_normal.jpeg)        sja_super03     이지은  Sun Oct 07 15:44:49 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2691041885/83859a1bf7d4a734615dc3483147e837_normal.jpeg)        sja_super04     이지현  Sun Oct 07 15:56:13 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2691074272/e70c7b9cef775cc70c597cc44a1f69d3_normal.png) sja_super05     김은진  Sun Oct 07 16:06:12 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2694507802/c74ecc97c2ff0ce96c6b9d15b597f063_normal.jpeg)        sja_super06     이지수  Mon Oct 08 13:38:31 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2694552203/5d60927c1672c67fb0aa4edc94734d46_normal.jpeg)        sja_super07     이지은  Mon Oct 08 13:53:17 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2694577786/9bb7015096fbb520594bd52c10621c69_normal.jpeg)        sja_super08     이진희  Mon Oct 08 14:00:42 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2694600592/83859a1bf7d4a734615dc3483147e837_normal.jpeg)        sja_super09     이수지  Mon Oct 08 14:07:31 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2694627655/c74ecc97c2ff0ce96c6b9d15b597f063_normal.jpeg)        sja_super10     이수현  Mon Oct 08 14:15:36 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2694699470/97556606b9429639a471b787ff5f2c3a_normal.jpeg)        pplced01        이수정  Mon Oct 08 14:37:45 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2694716209/b6ef314f340f03dd97f5d34433b25ad2_normal.jpeg)        pplced02        이지현  Mon Oct 08 14:42:15 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2694738621/83859a1bf7d4a734615dc3483147e837_normal.jpeg)        pplced03        김지원  Mon Oct 08 14:48:41 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2694763604/547ac5a3c1dcd47f51925e47eafbda6d_normal.jpeg)        pplced04        이수지  Mon Oct 08 14:54:59 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2694782462/3a8433962f2e11bcccf5f6993ab10bc5_normal.jpeg)        pplced05        이보현  Mon Oct 08 15:02:08 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2700984509/b6ef314f340f03dd97f5d34433b25ad2_normal.jpeg)        jolocdef02      이지수  Wed Oct 10 06:24:42 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2700996391/83859a1bf7d4a734615dc3483147e837_normal.jpeg)        jolocdef03      이현지  Wed Oct 10 06:31:17 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2701006976/a20bc0fcbad87f455749a9d267863d43_normal.jpeg)        jolocdef04      이하라  Wed Oct 10 06:37:15 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2701018808/3a8433962f2e11bcccf5f6993ab10bc5_normal.jpeg)        jolocdef05       김지현 Wed Oct 10 06:44:12 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2682631772/97556606b9429639a471b787ff5f2c3a_normal.jpeg)        johanblum01     이진영  Fri Oct 05 08:22:31 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2682647386/b6ef314f340f03dd97f5d34433b25ad2_normal.jpeg)        johanblum02     이수진  Fri Oct 05 08:31:27 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2682660030/841ac58975f8a35090620dbac0e41dac_normal.jpeg)        johanblum03     이지현  Fri Oct 05 08:38:58 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2682669696/a20bc0fcbad87f455749a9d267863d43_normal.jpeg)        johanblum04     김하연  Fri Oct 05 08:44:43 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2682677429/3a8433962f2e11bcccf5f6993ab10bc5_normal.jpeg)        johanblum05     이현지  Fri Oct 05 08:49:12 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2658416202/83859a1bf7d4a734615dc3483147e837_normal.jpeg)        kkancho01       김지은  Fri Sep 28 12:31:19 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2658424915/b6ef314f340f03dd97f5d34433b25ad2_normal.jpeg)        kkancho02       이정현  Fri Sep 28 12:34:56 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2658433403/97556606b9429639a471b787ff5f2c3a_normal.jpeg)        kkancho03       이지은  Fri Sep 28 12:38:02 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2658467107/a20bc0fcbad87f455749a9d267863d43_normal.jpeg)        kkancho04       이래원  Fri Sep 28 12:51:50 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2658478750/3a8433962f2e11bcccf5f6993ab10bc5_normal.jpeg)        kkancho05       김지연  Fri Sep 28 12:56:43 +0000 2012 <br>
![](http://abs.twimg.com/sticky/default_profile_images/default_profile_6_normal.png)    ccc_test2       지현    Sun Jan 06 15:00:48 +0000 2013 <br>
![](http://pbs.twimg.com/profile_images/2602146117/fdgfw5n9tt6z5ogfdmim_normal.jpeg)    smart__hyun     현♥     Wed Aug 29 05:23:31 +0000 2012 <br>
![](http://pbs.twimg.com/profile_images/2602234812/88888_normal.jpg)    perfect_girlvv  이주은  Wed Sep 12 12:13:18 +0000 2012 <br>
![](http://abs.twimg.com/sticky/default_profile_images/default_profile_4_normal.png)    in_parm 슈나    Thu Sep 20 08:43:20 +0000 2012 <br>
![](http://abs.twimg.com/sticky/default_profile_images/default_profile_3_normal.png)    sole_heart1129  콜탐    Thu Sep 20 08:51:28 +0000 2012 <br>
![](http://abs.twimg.com/sticky/default_profile_images/default_profile_5_normal.png)    im_whitecolor   하얀    Thu Sep 20 08:30:22 +0000 2012 <br>

