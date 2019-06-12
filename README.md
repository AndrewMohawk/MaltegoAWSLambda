# MaltegoAWSLambda
Cloudformation setup and Lambda function for writing Maltego transforms with AWS

# Setup
Go to cloudformation https://console.aws.amazon.com/cloudformation/home and upload the YAML file, complete with logging/AIM/lambda and API gateway setup.

Copy the 'apiGatewayInvokeURL' from the outputs window to be used with the Maltego TDS ( https://cetas.paterva.com/TDS/ )

Add a new transform on the Maltego TDS ( https://cetas.paterva.com/TDS/ ) with the URL as the above, usually something like https://hw7xxxxxxx8.execute-api.us-east-1.amazonaws.com/MaltegoTransform 

*NOTE:* you must select 'do not test this transform' when adding it.

Select the URL for the seed that you added the transform to and add that to Maltego.

Enjoi!

# Lambda Function
The Lambda files are already stored as a zip at https://maltegolambda.s3.amazonaws.com/MaltegoLambda.zip but feel free to put them somewhere else to store.

# Writing transform
Modify the transform code as neccessary in your Lambda section of AWS ( https://console.aws.amazon.com/lambda/home ) by editing the `sampleTransform` or create your own and call it from the `handler` function.

# Debugging transforms
Either test it via Lambda or you can also curl directly to the transform to test

`curl -d @data.xml -X POST https://rsfoaqubpl.execute-api.us-east-1.amazonaws.com/call/`

@data can be found at https://gist.github.com/AndrewMohawk/94476fed9fb58184f3f3bc1cb8372ff9/
