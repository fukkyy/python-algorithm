import socialStream

social=socialStream.socialStream()

url_list=social.userTimelineToUrl(access_token_key='94355673-WphJCUYWbjzQ0UisZJX2I2LaQuwlbK3fo7CRDEm3A',access_token_secret='Obq4CA7dRcbFXJl6KO0EHFYQbx6SuSIg9rciBN6Rs')

real_url_list=social.getRealUrl(url_list)

print real_url_list
