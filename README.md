# Upload_to_s3
## Project overview
| AWS | 
| PYTHON |
| S3 |
| PRESIGNED URL | 
| FLASK |

Upload files to AWS S3 with presigned URL using an interactive console. Done using a Flask Webapp structure 
### Intro 
The start of many projects/apps requires the uploading of an object to a database/storage facility either for analysis or long-term storage. This documentation provides the barebones structure for an interactive console to upload files to AWS S3 cloud storage using presigned URL. 

### Prerequisites
* An AWS Account 
* An IAM role attached to the EC2 instance with the following permission:
  * AmazonS3FullAccess

The IAM role ensures that no credentials have to be hard-coded to allow access to your s3 bucket. The application instead queries the instance metadata to obtain credentials when they are needed. 
The presigned URL generates a temporary access based on the credentials found in your instance metadata. For this app, the temporary access has been set to 3600s.

### Front-end display
![upload]

![save]











[upload]: https://i.imgur.com/JZrKRav.jpg
[save]: https://i.imgur.com/CXV1YsV.jpg


