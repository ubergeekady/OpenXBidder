# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='ssrtb.proto',
  package='',
  serialized_pb='\n\x0bssrtb.proto\"F\n\x04\x41\x64Id\x12\x13\n\x0b\x63\x61mpaign_id\x18\x01 \x02(\x05\x12\x14\n\x0cplacement_id\x18\x02 \x02(\x05\x12\x13\n\x0b\x63reative_id\x18\x03 \x02(\x05\"\x88\x01\n\x03Geo\x12\x0b\n\x03lat\x18\x01 \x01(\x02\x12\x0b\n\x03lon\x18\x02 \x01(\x02\x12\x0f\n\x07\x63ountry\x18\x03 \x01(\t\x12\x0c\n\x04\x63ity\x18\x04 \x01(\t\x12\x0b\n\x03zip\x18\x05 \x01(\t\x12\x0c\n\x04type\x18\x06 \x01(\x05\x12\x11\n\tcontinent\x18\x07 \x01(\t\x12\r\n\x05state\x18\x08 \x01(\t\x12\x0b\n\x03\x64ma\x18\t \x01(\x05\"\x91\x02\n\x06\x44\x65vice\x12\x0f\n\x07\x64idsha1\x18\x01 \x01(\t\x12\x0b\n\x03\x64nt\x18\x02 \x01(\x05\x12\n\n\x02ua\x18\x03 \x01(\t\x12\n\n\x02ip\x18\x04 \x01(\t\x12\x0f\n\x07\x63\x61rrier\x18\x05 \x01(\t\x12\n\n\x02os\x18\x06 \x01(\t\x12\x0b\n\x03osv\x18\x07 \x01(\t\x12\x10\n\x08language\x18\x08 \x03(\t\x12\x0c\n\x04make\x18\t \x01(\t\x12\r\n\x05model\x18\n \x01(\t\x12\x16\n\x0e\x63onnectiontype\x18\x0b \x01(\t\x12\x16\n\x0e\x64\x65precated_api\x18\x0c \x01(\t\x12\x11\n\x03geo\x18\r \x01(\x0b\x32\x04.Geo\x12\x0f\n\x07\x62rowser\x18\x0e \x01(\t\x12\x17\n\x0f\x62rowser_version\x18\x0f \x01(\t\x12\x0b\n\x03\x61pi\x18\x10 \x03(\x05\"\x9a\x05\n\nBidRequest\x12\x13\n\x0b\x61pi_version\x18\x01 \x02(\x05\x12\x12\n\nauction_id\x18\x02 \x02(\t\x12\x1e\n\x0fmatching_ad_ids\x18\x03 \x03(\x0b\x32\x05.AdId\x12\x16\n\x0epub_website_id\x18\x04 \x02(\t\x12\x11\n\tad_height\x18\x05 \x02(\x05\x12\x10\n\x08\x61\x64_width\x18\x06 \x02(\x05\x12\x16\n\x0euser_cookie_id\x18\x07 \x01(\t\x12\x17\n\x0fuser_ip_address\x18\x08 \x01(\x0c\x12\x1a\n\x12user_screen_height\x18\t \x01(\x05\x12\x19\n\x11user_screen_width\x18\n \x01(\x05\x12\x18\n\x10user_geo_country\x18\x0b \x01(\t\x12\x16\n\x0euser_geo_state\x18\x0c \x01(\t\x12\x14\n\x0cuser_geo_dma\x18\r \x01(\x05\x12\x12\n\nuser_agent\x18\x0e \x01(\t\x12\x11\n\tuser_lang\x18\x0f \x03(\t\x12\x0b\n\x03url\x18\x10 \x01(\t\x12\x14\n\x0chttp_referer\x18\x11 \x01(\t\x12\x15\n\rox_cat_tier_1\x18\x12 \x01(\x05\x12\x15\n\rox_cat_tier_2\x18\x13 \x01(\x05\x12\x17\n\x0fpub_blocked_cat\x18\x14 \x03(\x05\x12\x1b\n\x13pub_blocked_content\x18\x15 \x03(\x05\x12\x18\n\x10pub_blocked_type\x18\x16 \x03(\x05\x12\x17\n\x0fpub_blocked_url\x18\x17 \x03(\t\x12\x10\n\x08rtb_data\x18\x18 \x01(\t\x12 \n\x18pub_allowed_ad_languages\x18\x19 \x03(\t\x12\x17\n\x0fmarket_operator\x18\x1a \x01(\t\x12\x17\n\x06\x64\x65vice\x18\x1b \x01(\x0b\x32\x07.Device\x12\x0f\n\x07is_test\x18\x1c \x01(\x08\"\x94\x03\n\x0b\x42idResponse\x12\x13\n\x0b\x61pi_version\x18\x01 \x02(\x05\x12\x12\n\nauction_id\x18\x02 \x02(\t\x12(\n\x19\x44\x45PRECATED_matching_ad_id\x18\x03 \x01(\x0b\x32\x05.AdId\x12!\n\x19\x44\x45PRECATED_cpm_bid_micros\x18\x04 \x01(\x03\x12\x1a\n\x12\x44\x45PRECATED_ad_code\x18\x05 \x01(\t\x12\x1c\n\x14\x44\x45PRECATED_click_url\x18\x06 \x01(\t\x12 \n\x18\x44\x45PRECATED_advertiser_id\x18\x07 \x01(\t\x12\x1d\n\x15\x44\x45PRECATED_ad_ox_cats\x18\x08 \x03(\x05\x12%\n\x1d\x44\x45PRECATED_click_through_urls\x18\t \x03(\t\x12\x1b\n\x13\x44\x45PRECATED_buyer_id\x18\n \x01(\t\x12\x1b\n\x13\x44\x45PRECATED_brand_id\x18\x0b \x01(\t\x12\x12\n\x04\x62ids\x18\x0c \x03(\x0b\x32\x04.Bid\x12\x1f\n\x17next_highest_bid_micros\x18\r \x01(\x03\"\xa1\x01\n\x03\x42id\x12\x1d\n\x0ematching_ad_id\x18\x01 \x02(\x0b\x32\x05.AdId\x12\x16\n\x0e\x63pm_bid_micros\x18\x02 \x02(\x03\x12\x0f\n\x07\x61\x64_code\x18\x03 \x02(\t\x12\x12\n\nad_ox_cats\x18\x04 \x03(\x05\x12\x1a\n\x12\x63lick_through_urls\x18\x05 \x03(\t\x12\x10\n\x08\x62uyer_id\x18\x06 \x01(\t\x12\x10\n\x08\x62rand_id\x18\x07 \x01(\t\"Z\n\x0e\x41uctionResults\x12\x13\n\x0b\x61pi_version\x18\x01 \x02(\x05\x12\x12\n\nauction_id\x18\x02 \x02(\t\x12\x1f\n\x07results\x18\x03 \x03(\x0b\x32\x0e.AuctionResult\"\xb4\x01\n\rAuctionResult\x12\x1d\n\x0ematching_ad_id\x18\x01 \x02(\x0b\x32\x05.AdId\x12\x1e\n\x06status\x18\x02 \x02(\x0e\x32\x0e.AuctionStatus\x12\x13\n\x0bloss_reason\x18\x03 \x01(\t\x12\x14\n\x0c\x65rror_reason\x18\x04 \x01(\t\x12\x1a\n\x12winning_bid_micros\x18\x05 \x01(\x03\x12\x1d\n\x15\x63learing_price_micros\x18\x06 \x01(\x03*-\n\rAuctionStatus\x12\x07\n\x03win\x10\x01\x12\x08\n\x04loss\x10\x02\x12\t\n\x05\x65rror\x10\x03')

_AUCTIONSTATUS = descriptor.EnumDescriptor(
  name='AuctionStatus',
  full_name='AuctionStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='win', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='loss', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='error', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2017,
  serialized_end=2062,
)


win = 1
loss = 2
error = 3



_ADID = descriptor.Descriptor(
  name='AdId',
  full_name='AdId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='campaign_id', full_name='AdId.campaign_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='placement_id', full_name='AdId.placement_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='creative_id', full_name='AdId.creative_id', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=15,
  serialized_end=85,
)


_GEO = descriptor.Descriptor(
  name='Geo',
  full_name='Geo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='lat', full_name='Geo.lat', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lon', full_name='Geo.lon', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='country', full_name='Geo.country', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='city', full_name='Geo.city', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='zip', full_name='Geo.zip', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='Geo.type', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='continent', full_name='Geo.continent', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='state', full_name='Geo.state', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dma', full_name='Geo.dma', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=88,
  serialized_end=224,
)


_DEVICE = descriptor.Descriptor(
  name='Device',
  full_name='Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='didsha1', full_name='Device.didsha1', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dnt', full_name='Device.dnt', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ua', full_name='Device.ua', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ip', full_name='Device.ip', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='carrier', full_name='Device.carrier', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='os', full_name='Device.os', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='osv', full_name='Device.osv', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='language', full_name='Device.language', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='make', full_name='Device.make', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='model', full_name='Device.model', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='connectiontype', full_name='Device.connectiontype', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='deprecated_api', full_name='Device.deprecated_api', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='geo', full_name='Device.geo', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='browser', full_name='Device.browser', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='browser_version', full_name='Device.browser_version', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='api', full_name='Device.api', index=15,
      number=16, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=227,
  serialized_end=500,
)


_BIDREQUEST = descriptor.Descriptor(
  name='BidRequest',
  full_name='BidRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='api_version', full_name='BidRequest.api_version', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='auction_id', full_name='BidRequest.auction_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='matching_ad_ids', full_name='BidRequest.matching_ad_ids', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pub_website_id', full_name='BidRequest.pub_website_id', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ad_height', full_name='BidRequest.ad_height', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ad_width', full_name='BidRequest.ad_width', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_cookie_id', full_name='BidRequest.user_cookie_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_ip_address', full_name='BidRequest.user_ip_address', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_screen_height', full_name='BidRequest.user_screen_height', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_screen_width', full_name='BidRequest.user_screen_width', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_geo_country', full_name='BidRequest.user_geo_country', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_geo_state', full_name='BidRequest.user_geo_state', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_geo_dma', full_name='BidRequest.user_geo_dma', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_agent', full_name='BidRequest.user_agent', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_lang', full_name='BidRequest.user_lang', index=14,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='url', full_name='BidRequest.url', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='http_referer', full_name='BidRequest.http_referer', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ox_cat_tier_1', full_name='BidRequest.ox_cat_tier_1', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ox_cat_tier_2', full_name='BidRequest.ox_cat_tier_2', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pub_blocked_cat', full_name='BidRequest.pub_blocked_cat', index=19,
      number=20, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pub_blocked_content', full_name='BidRequest.pub_blocked_content', index=20,
      number=21, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pub_blocked_type', full_name='BidRequest.pub_blocked_type', index=21,
      number=22, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pub_blocked_url', full_name='BidRequest.pub_blocked_url', index=22,
      number=23, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rtb_data', full_name='BidRequest.rtb_data', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pub_allowed_ad_languages', full_name='BidRequest.pub_allowed_ad_languages', index=24,
      number=25, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='market_operator', full_name='BidRequest.market_operator', index=25,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='device', full_name='BidRequest.device', index=26,
      number=27, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_test', full_name='BidRequest.is_test', index=27,
      number=28, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=503,
  serialized_end=1169,
)


_BIDRESPONSE = descriptor.Descriptor(
  name='BidResponse',
  full_name='BidResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='api_version', full_name='BidResponse.api_version', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='auction_id', full_name='BidResponse.auction_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='DEPRECATED_matching_ad_id', full_name='BidResponse.DEPRECATED_matching_ad_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='DEPRECATED_cpm_bid_micros', full_name='BidResponse.DEPRECATED_cpm_bid_micros', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='DEPRECATED_ad_code', full_name='BidResponse.DEPRECATED_ad_code', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='DEPRECATED_click_url', full_name='BidResponse.DEPRECATED_click_url', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='DEPRECATED_advertiser_id', full_name='BidResponse.DEPRECATED_advertiser_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='DEPRECATED_ad_ox_cats', full_name='BidResponse.DEPRECATED_ad_ox_cats', index=7,
      number=8, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='DEPRECATED_click_through_urls', full_name='BidResponse.DEPRECATED_click_through_urls', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='DEPRECATED_buyer_id', full_name='BidResponse.DEPRECATED_buyer_id', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='DEPRECATED_brand_id', full_name='BidResponse.DEPRECATED_brand_id', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bids', full_name='BidResponse.bids', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='next_highest_bid_micros', full_name='BidResponse.next_highest_bid_micros', index=12,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1172,
  serialized_end=1576,
)


_BID = descriptor.Descriptor(
  name='Bid',
  full_name='Bid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='matching_ad_id', full_name='Bid.matching_ad_id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cpm_bid_micros', full_name='Bid.cpm_bid_micros', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ad_code', full_name='Bid.ad_code', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ad_ox_cats', full_name='Bid.ad_ox_cats', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='click_through_urls', full_name='Bid.click_through_urls', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='buyer_id', full_name='Bid.buyer_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='brand_id', full_name='Bid.brand_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1579,
  serialized_end=1740,
)


_AUCTIONRESULTS = descriptor.Descriptor(
  name='AuctionResults',
  full_name='AuctionResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='api_version', full_name='AuctionResults.api_version', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='auction_id', full_name='AuctionResults.auction_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='results', full_name='AuctionResults.results', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1742,
  serialized_end=1832,
)


_AUCTIONRESULT = descriptor.Descriptor(
  name='AuctionResult',
  full_name='AuctionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='matching_ad_id', full_name='AuctionResult.matching_ad_id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='status', full_name='AuctionResult.status', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='loss_reason', full_name='AuctionResult.loss_reason', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='error_reason', full_name='AuctionResult.error_reason', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='winning_bid_micros', full_name='AuctionResult.winning_bid_micros', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='clearing_price_micros', full_name='AuctionResult.clearing_price_micros', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1835,
  serialized_end=2015,
)

_DEVICE.fields_by_name['geo'].message_type = _GEO
_BIDREQUEST.fields_by_name['matching_ad_ids'].message_type = _ADID
_BIDREQUEST.fields_by_name['device'].message_type = _DEVICE
_BIDRESPONSE.fields_by_name['DEPRECATED_matching_ad_id'].message_type = _ADID
_BIDRESPONSE.fields_by_name['bids'].message_type = _BID
_BID.fields_by_name['matching_ad_id'].message_type = _ADID
_AUCTIONRESULTS.fields_by_name['results'].message_type = _AUCTIONRESULT
_AUCTIONRESULT.fields_by_name['matching_ad_id'].message_type = _ADID
_AUCTIONRESULT.fields_by_name['status'].enum_type = _AUCTIONSTATUS
DESCRIPTOR.message_types_by_name['AdId'] = _ADID
DESCRIPTOR.message_types_by_name['Geo'] = _GEO
DESCRIPTOR.message_types_by_name['Device'] = _DEVICE
DESCRIPTOR.message_types_by_name['BidRequest'] = _BIDREQUEST
DESCRIPTOR.message_types_by_name['BidResponse'] = _BIDRESPONSE
DESCRIPTOR.message_types_by_name['Bid'] = _BID
DESCRIPTOR.message_types_by_name['AuctionResults'] = _AUCTIONRESULTS
DESCRIPTOR.message_types_by_name['AuctionResult'] = _AUCTIONRESULT

class AdId(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ADID
  
  # @@protoc_insertion_point(class_scope:AdId)

class Geo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GEO
  
  # @@protoc_insertion_point(class_scope:Geo)

class Device(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DEVICE
  
  # @@protoc_insertion_point(class_scope:Device)

class BidRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BIDREQUEST
  
  # @@protoc_insertion_point(class_scope:BidRequest)

class BidResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BIDRESPONSE
  
  # @@protoc_insertion_point(class_scope:BidResponse)

class Bid(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BID
  
  # @@protoc_insertion_point(class_scope:Bid)

class AuctionResults(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUCTIONRESULTS
  
  # @@protoc_insertion_point(class_scope:AuctionResults)

class AuctionResult(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUCTIONRESULT
  
  # @@protoc_insertion_point(class_scope:AuctionResult)

# @@protoc_insertion_point(module_scope)
