NAME=sakura-vps-client-py

all: download_spec extract_cc_spec generate_models modify_gitignore put_readme

put_readme:
	./put_readme.sh;

modify_gitignore:
	echo /.idea >> .gitignore
	

generate_models: spec/spec.json
	openapi-generator generate \
		-i spec/spec.json \
		-g python \
		--package-name sakura_vps_client_py \
		--git-repo-id sakura_vps_client_py \
		--git-user-id g1eng \
		-o .

download_spec:
	[ -d spec ] || mkdir spec \
	&& curl -fSL -o spec/openapi.json https://manual.sakura.ad.jp/vps/api/api-doc/api-json.json

extract_cc_spec:
	./extract_spec_cc.sh

clean:
	rm -rv *.py README.md api docs spec test pyproject.toml requirements.txt sakura-vps-client-py setup.* test-requirements.txt tox.ini
