from snqueue.email import S3Email

profile_name = 'terminus'
bucket = 'incoming-mail-littledumb'
key = '9pn0jp31nms19ht1pr4p47hjlh6vkkvamk1p3bo1'

with S3Email(profile_name, bucket, key) as email:
  print(email.email)

