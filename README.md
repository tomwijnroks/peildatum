# peildatum
Files for the Bitcoin [peildatum](https://peildatum.nl) site.

# Generate (new) data
Collects data from the exchange API's or uses already existing data if no data came back from the API.

Needs python 3, which can be installed via [pyenv](https://github.com/pyenv/pyenv).

- Install dependencies `pip install -r requirements.txt`
- Collect new data `python collect.py`

# Generating the html
To generate the html and assets [Jekyll](https://jekyllrb.com) is used. This can generate the static html based on the OHLC yaml files.
When the page is hosted on [Github Pages](https://docs.github.com/en/pages), this is done automatically.

The `docs` dir contains the website source because this is the only allowed subdirectoty that GitHub pages can build from, according to the [documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#about-publishing-sources).

## Building the page
To build the page you need ruby. This can be installed with [rbenv](https://github.com/rbenv/rbenv).

Install and prepare a specific ruby version, install the bundler gem to manage dependencies and install the dependencies.
```
rbenv install 2.7.2
gem install bundler
bundle install
```

For Debian-like systems install as root (or use sudo):
```
apt install ruby2.7 ruby2.7-dev
gem install bundler jekyll
```
Switch to or login as the user, set the .gem path and run bundle install:
```
bundle config set --local path /home/username/.gem
bundle install
```

### Developing locally
When developing, start the Jekyll server that will auto rebuild and reload the page upon changes.
```
bundle exec jekyll serve --livereload --source ./docs
```
The page can now be accessed at [http://127.0.0.1:4000](http://127.0.0.1:4000).

### Building for production
When *not* using GitHub pages to host the website, the site needs to be build (on the server) when there are changes.
Building for production will generate the html once and write all files in the `_site` dir which then needs to be serverd by apache/nginx/etc.
```
bundle exec jekyll build --source ./docs
```
