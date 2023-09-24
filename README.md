# streamzero-streamlit-s3-uploader
A generic UI to upload files to AWS S3 or S3 Compatible Storage (such as MinIO) for quick tests.

The following are the environment parameters to be set

```
        env:
        - name: MINIO_ENDPOINT
          value: "http://fx-minio.core:9000"
        - name: MINIO_ACCESS_KEY
          value: "miniofx"
        - name: MINIO_SECRET_KEY
          value: "minio123"
        - name: MINIO_BUCKET_NAME
          value: "generic"
        - name: TARGET_BUCKETS
          value: "generic,whisper-in"   

```
