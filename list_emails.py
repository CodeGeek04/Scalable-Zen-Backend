import firebase_admin
from firebase_admin import credentials, storage

def get_all_owners():
    bucket = storage.bucket()
    blobs = bucket.list_blobs()

    # Extract the name of each blob (which is the email in your case)
    emails = [blob.name for blob in blobs]
    return emails

def get_all_emails():
    bucket = storage.bucket()
    blobs = bucket.list_blobs(prefix='Alternate_Emails/')  # List blobs inside the 'Alternate_Emails' folder

    # Extract the name of each blob
    emails = [blob.name.replace('Alternate_Emails/', '') for blob in blobs]  # Removing the folder prefix to get the email names
    return emails

def delete_email_from_storage(email):
    """
    Delete a specific email-credential pair from Firebase Cloud Storage.
    """
    bucket = storage.bucket()
    blob = bucket.blob(email)  # Get a reference to the blob
    blob.delete()              # Delete the blob

    print(f"Deleted {email} from storage.")

def add_alternate_email(alternate_email, owner_email):
    """
    Add an alternate email inside the Alternate_Emails folder in Firebase Cloud Storage.
    
    :param alternate_email: The name of the file to be created.
    :param owner_email: The content of the file, representing the owner's email.
    """
    bucket = storage.bucket()

    # Create a blob reference inside the Alternate_Emails folder
    blob = bucket.blob(f'Alternate_Emails/{alternate_email}')

    # Upload the owner_email as the content of the blob
    blob.upload_from_string(owner_email)

    print(f"Added {alternate_email} with owner email {owner_email} to storage.")

def get_owner_email(alternate_email):
    """
    Retrieve the owner email using the alternate email from the Alternate_Emails folder in Firebase Cloud Storage.
    
    :param alternate_email: The name of the file to fetch.
    :return: The owner email (content of the file).
    """
    bucket = storage.bucket()

    # Create a blob reference inside the Alternate_Emails folder
    blob = bucket.blob(f'Alternate_Emails/{alternate_email}')

    # Download the content of the blob
    owner_email = blob.download_as_text()

    return owner_email

def delete_alternate_email(alternate_email):
    """
    Delete a specific alternate email or all alternate emails from the Alternate_Emails folder in Firebase Cloud Storage.
    
    :param alternate_email: The name of the file to be deleted or "all" to delete all files.
    """
    bucket = storage.bucket()

    if alternate_email == "all":
        # Delete all blobs inside the Alternate_Emails folder
        blobs = bucket.list_blobs(prefix='Alternate_Emails/')
        for blob in blobs:
            blob.delete()
        print("Deleted all alternate emails from storage.")
    else:
        # Delete the specific blob named after the alternate_email
        blob = bucket.blob(f'Alternate_Emails/{alternate_email}')
        blob.delete()
        print(f"Deleted {alternate_email} from storage.")

if __name__ == "__main__":
    cred = credentials.Certificate('firebase_secrets.json')
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'userbot-285810.appspot.com'
    })
    delete_alternate_email("all")
    add_alternate_email("shivam@elysiuminnovations.ai", "shivam@elysiuminnovations.ai")
    add_alternate_email("arben@elysiuminnovations.ai", "arben@elysiuminnovations.ai")
    add_alternate_email("michael.gruen9@gmail.com", "michael@elysiuminnovations.ai")
    print(get_all_emails())
    # print(get_owner_email("shivammittal2124@gmail.com"))