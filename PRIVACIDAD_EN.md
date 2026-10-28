# Críptico Club Privacy Policy

**Review version:** October 28, 2026  
**Service:** Críptico Club — Discord Activity  
**Language:** English · [Español](../../privacidad/)  
**Terms of Service:** [Read](../terms/)

## 1. Controller and contact

The controller of personal data handled by Críptico Club is **Antonio Pérez Serrano**, acting as an individual under the trading name **Zerep Games**, which is not a separate legal entity.

**Address supplied by the provider:** Calle Licenciado Cascales, 30260, Murcia, Spain.

**Privacy requests and general contact:** **zerep.a.p.s@gmail.com** (recommended subject: **“Support CripticoClub”**).

Discord handles information relating to its own platform under its own Privacy Policy. Críptico Club does not control Discord's independent processing activities.

## 2. Categories of personal data

- **Discord identity:** a stable Discord user ID, username, avatar and, when server access is verified, guild identifiers and membership status. We do not ask for your Discord password or read private messages.
- **Gameplay:** selected language, daily challenges, wrong answers, hints used, revealed letters, scores, XP, streaks, history and statistics needed for global and server leaderboards.
- **Premium access:** Discord SKU and entitlement identifiers, dates of validity, expiry, revocation and last verification. We do not collect full credit-card details.
- **Contributions:** submitted clue text, answer, explanation, language, difficulty, public credit or anonymity choice, editorial status, submission and review dates, moderator notes and evidence of the license agreed. The author's public username may be saved as a fixed snapshot.
- **Acceptance records:** account identifier, date and version of Terms accepted. Agreeing to publish a submitted work or authorize potential AI-related exploitation is distinct from granting any authorization needed to process personal data.
- **Technical events:** random request IDs, HTTP route templates, method, status, processing times, aggregate metrics and errors. The API is designed to exclude tokens and Discord IDs from these records; the hosting proxy and third-party services may process IP addresses and other network metadata.

The frontend's font files are self-hosted and do not require connections to Google Fonts.

## 3. Purposes and legal bases

| Purpose                                                                                   | Proposed legal basis                                                                                                                           |
| ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Discord authentication, daily gameplay, progress, profiles, leaderboards and history      | Performance of the requested service (GDPR Article 6(1)(b)).                                                                                   |
| Recording acceptance of Terms and checking Premium access                                 | Contract performance and, when relevant, compliance with legal obligations (Articles 6(1)(b), 6(1)(c)).                                        |
| Receiving and reviewing voluntarily submitted puzzles, editorial attribution and licenses | Performance of contribution arrangements; applicable safeguards will be assessed for public attribution of user identifiers (Article 6(1)(b)). |
| Service security, misuse prevention, troubleshooting and defense of legal claims          | Proportionate legitimate interests (Article 6(1)(f)).                                                                                          |
| Required tax, accounting and lawful requests from public authorities                      | Compliance with legal obligations, where applicable (Article 6(1)(c)).                                                                         |

We do not use gameplay data for targeted advertising or send direct promotional messages from Zerep Games. Puzzle submission is not required to use the game.

## 4. Contributions and artificial intelligence

Puzzle submission is voluntary. **Submitting a contribution requires accepting a license to use the submitted content**, including advance contractual permission for the **clue text** to be used for possible AI model training or improvement in the future, under the Terms of Service. Playing does not require submitting a puzzle.

**No user-submitted puzzles are currently used for AI model training.** OpenAI is the intended provider for future editorial assistance, but the integration has not yet been deployed. Inputs sent to OpenAI's API are not used by default to train models unless the API customer opts in.

If an external editorial provider is introduced, the plan is to send **only the clue text**, after reviewing and removing any personal data found in it. Discord IDs, usernames, avatars, answers, explanations and other account information are not intended to be transmitted. A user may inadvertently enter personal data in the clue itself; the clue **cannot be presumed anonymous without prior review**.

Permission to exploit a copyrighted work does not replace the lawful basis required to process personal data contained in that work, or override GDPR rights. Before enabling external training in the future, applicable legal, contractual and technical conditions, rights and safeguards will be checked and this Policy will be updated where required.

## 5. Information visible to other players

Leaderboards, scores and statistics may be displayed in association with a Discord username. Pending submissions and internal moderator notes are not public.

Published puzzles show the **username that existed when the puzzle was submitted** by default, unless the contributor selected anonymity before submitting. This attribution is a snapshot, not an identity key; internal relations rely on the stable Discord ID. Changes to a user's Discord username do not automatically alter previous publication credits.

On account deletion, retained submissions are disconnected from the player's account and author identifiers are removed from the records covered by the implemented erasure process. Editorial versions already published with a separate author field may require additional handling. Copies previously shared on other platforms may remain in third-party archives, without prejudice to legally valid requests.

An accepted submission's scheduled publication date is not disclosed in advance. Acceptance does not guarantee publication. When internal notifications are introduced, approval notices will state only that the submission was accepted, without specifying its publication date.

## 6. Service providers and recipients

- **Discord:** login, verified server membership, Activity distribution, Premium purchases, billing and cancellation, under Discord's own terms.
- **Hosting infrastructure:** planned **Kubernetes deployment in Spain** with PostgreSQL in the cluster. The technical administrator will have infrastructure duties; **access to personal data and credentials must be restricted through separate permissions**, subject to validation before launch.
- **Cloudflare:** planned for **Tunnel, public proxy/access and protective services such as WAF**, according to features ultimately enabled. Cloudflare may process connection metadata that must be verified in the real configuration.
- **Grafana:** technical metrics and monitoring dashboards. Grafana is planned as an observability tool, not for behavioural advertising analytics. Its hosting and access model must be verified.
- **GitHub Pages:** publicly hosting these Terms and Privacy Policy. The service provider may process technical visitor information under its own terms.
- **OpenAI:** intended provider, **not yet integrated**, for future editorial assistance as described in section 4.

Technical access by collaborators and providers will be limited to what is needed for service delivery. We do not sell player data to advertisers.

## 7. International transfers

Discord, GitHub, Cloudflare or other providers may be involved in processing outside the European Economic Area. Hosting PostgreSQL in Spain does not by itself guarantee that all access to personal data will remain in Spain.

Before enabling integrations involving international transfers, we will assess the actual contracting entities, relevant countries, subprocessors and required safeguards, including adequacy decisions or contractual clauses where applicable. You may request information about active service providers by contacting the controller.

## 8. Data retention and erasure

| Category                                            | Processing and retention                                                                                                                                                                                                                     |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Accounts, progress and gameplay                     | Data is retained while the account is needed to provide the service and is erased following authenticated account deletion, subject to legal duties. **Automatic erasure after 24 months of inactivity is planned but not yet implemented.** |
| Pending submissions                                 | **Planned editorial limit: 90 days from submission** if still pending. Automatic age-based cleanup is not yet deployed.                                                                                                                      |
| Rejected submissions                                | **Planned editorial limit: 30 days after rejection**. Automatic cleanup is not yet deployed.                                                                                                                                                 |
| Approved but unpublished submissions                | **Planned editorial limit: up to 12 months after acceptance**. Automatic cleanup is not yet deployed.                                                                                                                                        |
| Published contributions                             | Content may be retained while a valid exploitation license remains in force. Account deletion disconnects proposal records from their author; separately stored published credits still require additional handling.                         |
| Editorial review notes                              | For published submissions, a **planned period of 30 days after publication**. Notes of rejected proposals follow the relevant rejection retention rule. Automatic rotation is not yet deployed.                                              |
| Internal approval, rejection and expiration notices | **30 days from notification**, once notifications become available. Users may currently consult proposal status, but automatic notices are not guaranteed.                                                                                   |
| Premium data                                        | Deleting a Críptico Club account removes locally stored Premium-access records, but **does not cancel Discord's billing**. Records required by law may be retained for mandatory periods.                                                    |
| Support and privacy requests                        | Target retention of **up to 12 months after closure**, unless legal duties or pending disputes justify a different retention period.                                                                                                         |
| Technical logs, metrics and traces                  | **Target rotation: 30 days**, to be verified for production hosting and aggregation systems.                                                                                                                                                 |
| Backups                                             | **Planned daily backups**, encrypted with a **maximum 30-day rotation** within the planned infrastructure. Deployment and restoration still need verification. Deleted data may remain temporarily in backups until their normal expiry.     |

We do not claim that an undeployed automatic erasure process is already functioning. Planned retention periods will become operational commitments once implemented and verified.

## 9. Account deletion and data-subject rights

An authenticated **“Delete account and data”** option is available in **Profile → Settings**, subject to confirmation. It removes account records, gameplay history, XP, streaks, stored server membership, local Premium entitlements and acceptance records. **Previously submitted cryptic puzzles can remain in the moderation system without their account link or author credit.** Separately stored editorial credits in already published versions may require additional treatment.

**Deleting Críptico Club data does not cancel a Discord Premium subscription.** Cancel the relevant subscription within Discord if you wish to stop future charges.

Depending on applicable law, you may request access, rectification, erasure, restriction, objection or portability and withdraw consent where personal-data processing actually relies on consent. Contact **zerep.a.p.s@gmail.com**. We may proportionately verify your identity before responding.

You may also submit a complaint to the [Spanish Data Protection Agency (AEPD)](https://www.aepd.es/).

## 10. Security, cookies and local technology

Access is verified through Discord and backend authorization controls. Activity session tokens are intended to remain temporary and in memory; we do not request your Discord password. The service uses technical request identifiers and checks to preserve integrity of gameplay and scoring.

We do not plan to use our own advertising pixels, marketing trackers or commercial profiling. Discord, Cloudflare, GitHub Pages and infrastructure security services may use cookies or other technical data under their own policies. Effective browser storage, logs and network calls will be audited before final launch.

## 11. Updates

We will publish a revised Policy if purposes, providers, data categories or retention periods change materially. Where legally required, affected users will receive further information or be asked for authorization before additional processing begins. The Spanish and English versions must remain materially equivalent.

**Contact:** **zerep.a.p.s@gmail.com**  
**Terms of Service:** [Read](../terms/)
