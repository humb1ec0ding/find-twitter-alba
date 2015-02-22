#!/usr/bin/env python
#-*- coding: utf-8 -*-

from birdy.twitter import UserClient

# Create Twitter Apps : https://apps.twitter.com/
client = UserClient(CONSUMER_KEY,
                    CONSUMER_SECRET,
                    ACCESS_TOKEN,
                    ACCESS_TOKEN_SECRET)

users = [
    'ohademayochuchu',
    'shinytart',
    #
    'tiny_farm1',
    'bonussa01',
    'bonussa02',
    'bonussa03',
    'bonussa04',
    'bonussa05',
    'kojisiktaxi01',
    'kojisiktaxi02',
    'kojisiktaxi04',
    'kojisiktaxi03',
    'sja_super01',
    'sja_super02',
    'sja_super03',
    'sja_super04',
    'sja_super05',
    'sja_super06',
    'sja_super07',
    'sja_super08',
    'sja_super09',
    'sja_super10',
    'pplced01',
    'pplced02',
    'pplced03',
    'pplced04',
    'pplced05',
    'jolocdef02',
    'jolocdef03',
    'jolocdef04',
    'jolocdef05',
    'johanblum01',
    'johanblum02',
    'johanblum03',
    'johanblum04',
    'johanblum05',
    'kkancho01',
    'kkancho02',
    'kkancho03',
    'kkancho04',
    'kkancho05',
    'ccc_test2',
    'smart__hyun',
    'perfect_girlvv',
    'in_parm',
    'sole_heart1129',
    'im_whitecolor'
]

#response = client.api.users.show.get(screen_name=user)
#print response.data

resource = client.api.users.show

for user in users:
    response = resource.get(screen_name=user)
    r = response.data
    print "![](%s)\t[%s](https://twitter.com/%s)\t%s\t%s <br>" % (r.profile_image_url, r.screen_name, r.screen_name, r.name, r.created_at)
#    print "\t%s" % r.screen_name
#    print "\t%s" % r.name
#    print "\t%s" % r.created_at
#    print "\tprofile_image_url\t= %s" % r.profile_image_url
