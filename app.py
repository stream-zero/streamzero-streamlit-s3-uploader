import streamlit as st
import boto3
import os


# Specify your credentials and custom endpoint here
aws_access_key_id = os.environ['MINIO_ACCESS_KEY']
aws_secret_access_key = os.environ['MINIO_SECRET_KEY']
endpoint_url = os.environ['MINIO_ENDPOINT']


# Initialize a session using Amazon S3
s3 = boto3.client('s3', 
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  endpoint_url=endpoint_url)


# Get the list of target buckets from environment variable
TARGET_BUCKETS = os.environ.get("TARGET_BUCKETS").split(",")

def main():
    st.title("S3 File Upload")

    # Create a file upload widget
    uploaded_file = st.file_uploader("Choose a file...")

    # Create a dropdown for selecting the target bucket
    target_bucket = st.selectbox("Select Target Bucket", TARGET_BUCKETS)

    if uploaded_file is not None:
        st.write("Uploaded file:", uploaded_file.name)

        # Create a button to upload the file to S3
        if st.button("Upload to S3"):
            try:
                # Upload the file to the selected bucket
                s3.upload_fileobj(uploaded_file, target_bucket, uploaded_file.name)
                st.success(f"File '{uploaded_file.name}' uploaded to {target_bucket} successfully!")
            except Exception as e:
                st.error(f"Error uploading file to S3: {str(e)}")

if __name__ == "__main__":
    main()
