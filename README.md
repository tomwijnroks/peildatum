# peildatum
Files for the Bitcoin [peildatum](https://peildatum.nl) site.

# Generate (new) data
Collects data from the exchange API's or uses already existing data if no data came back from the API.

Needs python 3, which can be installed via [pyenv](https://github.com/pyenv/pyenv).

- Install dependencies `pip install -r requirements.txt`
- Collect new data `python collect.py`

By default only new data for the last 2 years is being collected. If you want to get data for a specific year, add it as a commandline argument: `python collect.py 2018`. Or use `python collect.py all` to get data for all years, which is pretty slow.

## Kraken API limits
Kraken does not offer an easy way to get the OHLC info for all the years (only the last year or so). In order to get all OHLC data for a whole day, multiple API calls must be made to get all trades that happened that day. Because Kraken has a strict API rate limit, a delay/sleep had to be added. Getting Kraken data is therefore really slow, compared to the other exchanges.

# Generating the html
To generate the html and assets [Jekyll](https://jekyllrb.com) is used. This can generate the static html based on the OHLC yaml files.
When the page is hosted on [Github Pages](https://docs.github.com/en/pages), this is done automatically.

The `docs` dir contains the website source because this is the only allowed subdirectory that GitHub pages can build from, according to the [documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#about-publishing-sources).

## Building the page
To build the page you need ruby. This can be installed with [rbenv](https://github.com/rbenv/rbenv).

Install and prepare a specific ruby version, install the bundler gem to manage dependencies and install the dependencies.
```
rbenv install 3.2.6
gem install bundler
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
Building for production will generate the html once and write all files in the `_site` dir which then needs to be served by apache/nginx/etc.
```
bundle exec jekyll build --source ./docs
```
