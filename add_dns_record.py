import ovh

# Set your API credentials
client = ovh.Client(
    endpoint='ovh-eu',  # Change to 'ovh-us' if you are in North America
    application_key='YOUR_APPLICATION_KEY',
    application_secret='YOUR_APPLICATION_SECRET',
    consumer_key='YOUR_CONSUMER_KEY',
)

# Set the parameters for the DNS record
domain = 'yourdomain.com'
record_type = 'A'  # Change to the type of record you want to add (e.g., A, CNAME, MX, etc.)
sub_domain = 'www'  # Set to the subdomain you want to add, or leave empty for the root domain
target = '192.0.2.1'  # Set to the target IP address or hostname for the record
ttl = 3600  # Time-to-live in seconds

# Add the DNS record
try:
    result = client.post(f'/domain/zone/{domain}/record', fieldType=record_type, subDomain=sub_domain, target=target, ttl=ttl)
    print(f"DNS record added successfully: {result}")
except Exception as e:
    print(f"Error adding DNS record: {e}")

# Apply the changes
try:
    client.post(f'/domain/zone/{domain}/refresh')
    print("DNS zone refreshed successfully.")
except Exception as e:
    print(f"Error refreshing DNS zone: {e}")
