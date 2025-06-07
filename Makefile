NAME=sakura-vps-client-py
OPENAPI_VERSION=7.13.0

all: download_spec spec/spec-tmp.json diff_spec generate_models modify_gitignore put_readme

renew: download_spec spec/spec-tmp.json generate_models modify_gitignore put_readme

check_diff: download_spec spec/spec-tmp.json diff_spec 

put_readme:
	./scripts/put_readme.sh;

modify_gitignore:
	echo /.idea >> .gitignore
	echo .\*.swp >> .gitignore
	echo /spec/spec-tmp.json >> .gitignore
	echo /spec/openapi-next.json >> .gitignore
	echo /spec/openapi.json >> .gitignore
	

generate_models: spec/spec.json
	openapi-generator version | grep $(OPENAPI_VERSION)  || exit 1 \;
	openapi-generator generate \
		-i spec/spec.json \
		-g python \
		--package-name sakura_vps_client_py \
		--git-repo-id sakura_vps_client_py \
		--git-user-id g1eng \
		-o .

diff_spec:
	[ -f spec/spec.json ] \
		&& diff spec/spec.json spec/spec-tmp.json || exit 1

download_spec:
	[ -d spec ] || mkdir spec \
	&& curl -fSL -o spec/openapi.json https://manual.sakura.ad.jp/vps/api/api-doc/api-json.json


spec/spec-tmp.json: 
	./scripts/extract_spec_cc.sh spec/openapi-next.json spec/spec-tmp.json

clean:
	rm -rv *.py README.md api docs spec test pyproject.toml requirements.txt sakura-vps-client-py setup.* test-requirements.txt tox.ini
