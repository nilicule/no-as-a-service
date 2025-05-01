# No-As-A-Service

A simple API that returns random creative rejection reasons.

## API Endpoint

- `GET /no`: Returns a random rejection reason in JSON format.

Example response:
```json
{
  "reason": "This feels like something Future Me would yell at Present Me for agreeing to."
}
```

## Running with Podman

### Build the container

```bash
podman build -t no-as-a-service .
```

### Run the container

```bash
podman run -p 5001:5001 no-as-a-service
```

The API will be available at http://localhost:5001/no

## Testing the API

You can test the API using curl:

```bash
curl http://localhost:5001/no
```

Or open the URL in your browser: http://localhost:5001/no
