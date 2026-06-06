FROM public.ecr.aws/lambda/python:3.9

# Install system deps
RUN yum install -y gcc postgresql-devel && yum clean all

# Copy requirements first
COPY ./modules/users/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Set the CMD to your handler (file.function_name)
CMD ["app.lambda_handler"]