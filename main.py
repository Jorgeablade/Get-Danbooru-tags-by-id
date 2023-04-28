from pybooru import Danbooru
from dotenv import load_dotenv

import os
load_dotenv()

username = "YOUR-USERNAME"
apikey = os.environ.get("APIKEY")
id_psot = "THE-ID-OF-THE-POST"

client = Danbooru('danbooru', username=username, api_key=apikey)

post = client.post_show(post_id=id_psot)

tags = ("{0}, {1}, {2}, {3}".format(post['tag_string_general'], post['tag_string_character'], post['tag_string_copyright'], post['tag_string_artist']))

tags = tags.replace(",", "")
tags_with_commas = ", ".join(tags.split())

with open("tags.txt", "w") as f:
    f.write(tags_with_commas)
    
