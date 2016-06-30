clone-repo:
	gcloud source repos clone default --project=managedvm-provaric

push:
	git push -u origin master

deploy-hello-world:
	cd default/1-hello-world && make deploy