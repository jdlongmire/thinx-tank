# Thinx-Tank

A Hugo blog on IT, the digital enterprise, and applied AI. Published with
GitHub Pages at **https://blog.thinxai.net**.

## Run locally

Requires [Hugo](https://gohugo.io/installation/) (extended edition):

```bash
hugo server
```

Then open http://localhost:1313.

## Add a post

```bash
hugo new posts/your-slug.md
```

Edit the file under `content/posts/`, set `draft: false` in the front matter
when it's ready, commit, and push to `main`.

## Deploy

Pushing to `main` triggers `.github/workflows/hugo.yaml`: it installs Hugo
(extended), builds the site with `--minify`, and deploys the result to GitHub
Pages. No action needed beyond the push.

## Custom domain / DNS

The repo ships a `static/CNAME` file containing `blog.thinxai.net`, which
GitHub Pages uses to serve the site on that domain.

**One-time DNS step (owner action):** at your domain registrar, add a DNS
record:

- Type: `CNAME`
- Host/Name: `blog`
- Value: `jdlongmire.github.io`

GitHub will provision the HTTPS certificate automatically once the record
resolves (usually within minutes; can take up to a day).
