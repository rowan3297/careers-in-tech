
## Run the app locally

		docker-compose up

To build and run the app on localhost:5000.

## Run the app on a VM

Run the launch.sh shell script. Not tested in a while.

## Scraping jobs data - ignore

If using scrape jobs module, you need to use GCP API.

+ Set Google API environment variables:

		export GOOGLE_CLOUD_PROJECT="digital-skills-incubator"
		export GOOGLE_APPLICATION_CREDENTIALS=/path/to/API/key.json	
