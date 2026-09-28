---
name: adv3-cms-proxy-route-repair
description: Diagnose and repair ADV3 dashboard/API failures caused by CMS-managed proxy route drift. Use when an ADV3 host loads `/ad-dashboard/login` but `/ad-rest-api/v1/etl-info` or `/ad-rest-api/v1/publication-info` returns `404`, when `proxy_adv3.conf` may have changed on host, or when CMS templates for `${AD_CLT}/config/httpd/docker/conf` must be inspected, corrected, deployed, and revalidated.
disable-model-invocation: true
---

Run a narrow ADV3 proxy-repair workflow.

## Goal
- Restore ADV3 API routing behind the front `httpd` container.
- Fix the durable CMS template, not only the live deployed file.
- Verify the repair with the smallest useful endpoint checks first.

## Scope
- Treat `${AD_CLT}/config/httpd/docker/conf/proxy_adv3.conf` as the live routing file.
- Treat `${AD_CLT}/cms/template/AD_CLT/config/httpd/docker/conf/proxy_adv3.conf_tpl` as the persistent CMS source.
- Keep `${AD_CLT}/config/sysadm/docker/.env` in view for port and runtime context, but do not start there when the symptom is a proxy-path `404`.

## Use This Order
1. Confirm the symptom.
2. Inspect the live proxy file.
3. Compare or repair the CMS template.
4. Run `cms resolve_template` and `cms deploy_config`.
5. Recreate the stack with `./forge.sh -r`.
6. Re-verify `login`, `etl-info`, and `publication-info`.

## Symptom Triage
- Treat a loaded dashboard plus `publication-info` `404` as proxy drift first.
- Treat total HTTPS failure or load balancer restart as a different problem; inspect certs, container state, and logs before changing CMS templates.
- Treat `503` as a likely upstream/container health issue before editing routes.

## Live Inspection
Run these checks on the host before changing anything:

```bash
grep -n "/ad-dashboard" "$AD_CLT/config/httpd/docker/conf/proxy_adv3.conf"
grep -n "/ad-rest-api" "$AD_CLT/config/httpd/docker/conf/proxy_adv3.conf"
grep -n "ad_rest_api:8080" "$AD_CLT/config/httpd/docker/conf/proxy_adv3.conf"
curl -k -I "https://<fqdn>:<https_port>/ad-dashboard/login"
curl -k -I "https://<fqdn>:<https_port>/ad-rest-api/v1/etl-info"
curl -k -I "https://<fqdn>:<https_port>/ad-rest-api/v1/publication-info"
```

If the route markers are missing from the live proxy, inspect the CMS template next instead of patching only the deployed file.

## CMS Repair
- Edit `${AD_CLT}/cms/template/AD_CLT/config/httpd/docker/conf/proxy_adv3.conf_tpl`.
- Preserve the ADV3 dashboard route.
- Preserve the `/ad-rest-api` route to `ad_rest_api:8080`.
- Keep specific routes ahead of broad fallback routes.
- Avoid syncing a known-bad live proxy file back into the template unchanged.

Deploy the corrected template:

```bash
cms resolve_template "$AD_CLT/config/httpd/docker/conf"
cms deploy_config "$AD_CLT/config/httpd/docker/conf"
```

If `cms` is not in `PATH`:

```bash
export AD_SYSADM=<base>/sysadm
<base>/bin/cms resolve_template "$AD_CLT/config/httpd/docker/conf"
<base>/bin/cms deploy_config "$AD_CLT/config/httpd/docker/conf"
```

## Stack Recreate
From `$AD_SYSADM/adv3-docker`:

```bash
./forge.sh -r
```

After recreate, if the API is healthy but the dashboard still shows stale upstream behavior, restart only the front `httpd` container as a narrow follow-up.

## Verification
Use this order:

```bash
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
curl -k -I "https://<fqdn>:<https_port>/ad-dashboard/login"
curl -k -I "https://<fqdn>:<https_port>/ad-rest-api/v1/etl-info"
curl -k -I "https://<fqdn>:<https_port>/ad-rest-api/v1/publication-info"
curl -k -I "https://<fqdn>:<https_port>/ad-rest-api/v1/system-info"
```

- Treat `system-info` as advisory if the other endpoints are healthy.
- If `publication-info` remains `404`, compare the deployed proxy file with the CMS template and inspect `httpd` logs before changing more runtime config.

## Output
Return:
- symptom summary
- live files inspected
- template changes made
- CMS deploy commands run
- stack recreate status
- endpoint verification results
- remaining risks
- rollback

## Rollback
- Restore the previous `proxy_adv3.conf_tpl` from backup or versioned source.
- Run `cms resolve_template` and `cms deploy_config` again.
- Recreate the stack with `./forge.sh -r`.
