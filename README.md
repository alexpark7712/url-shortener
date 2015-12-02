### API

- google api key
  - AIzaSyA62lFjToSj8yGRr5KRDrtHTZemAz0tuhQ
- desc
  - https://developers.google.com/url-shortener/v1/getting_started

### Test

```bash
curl https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyA62lFjToSj8yGRr5KRDrtHTZemAz0tuhQ \
-H 'Content-Type: application/json' \
-d '{"longUrl": "http://www.google.com/"}'
```

### Test2