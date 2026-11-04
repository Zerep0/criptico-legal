# Críptico Club Privacy Policy

**Last updated:** November 4, 2026 · **Version:** 2026-11-04-v2
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
- **Premium and subscriptions:** if Premium is purchased through Discord, the game processes Discord-provided SKU and entitlement identifiers, validity periods, revocation status and last verification time to grant or remove subscriber benefits. Discord handles payments; we do not receive full payment-card numbers.
- **Contributions through Discord:** submissions are received through private tickets in the Discord server, managed by Tickets Tools. They may include Discord user ID/username, ticket messages and attachments, clue, answer, explanation, language, anonymity request, dates, decisions, review notes and evidence of express license acceptance. Published attribution may store a fixed username snapshot.
- **Acceptance records:** account identifier, date and version of Terms accepted. Acceptance of in-Activity Terms is separate from express acceptance of the contribution license in a Discord ticket; neither replaces the legal basis needed to process personal data.
- **Technical events:** API events (random request IDs, route, method, status, latency and errors) and operational Nginx logs on the Contabo VPS, which may contain IP addresses, dates, requests and connection metadata. Cloudflare may also process IP addresses and network metadata to deliver and protect the service. Application logs must not include tokens or credentials.

The frontend's font files are self-hosted and do not require connections to Google Fonts.

## 3. Purposes and legal bases

| Purpose                                                                                   | Proposed legal basis                                                                                                                           |
| ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Discord authentication, daily gameplay, progress, profiles, leaderboards and history      | Performance of the requested service (GDPR Article 6(1)(b)).                                                                                   |
| Recording acceptance of the Terms of Service | Contract performance and, where applicable, compliance with legal obligations (GDPR Articles 6(1)(b) and 6(1)(c)). |
| Receiving and reviewing voluntarily submitted puzzles, editorial attribution and licenses | Performance of contribution arrangements; applicable safeguards will be assessed for public attribution of user identifiers (Article 6(1)(b)). |
| Service security, misuse prevention, troubleshooting and defense of legal claims          | Proportionate legitimate interests (Article 6(1)(f)).                                                                                          |
| Required tax, accounting and lawful requests from public authorities                      | Compliance with legal obligations, where applicable (Article 6(1)(c)).                                                                         |

We do not use gameplay data for targeted advertising or send direct promotional messages from Zerep Games. Puzzle submission is not required to use the game.

## 4. Contributions and artificial intelligence

Puzzle submissions are voluntary and handled **through private tickets in the [official Discord server](https://discord.com/invite/5NccdaPNRM), not within the Activity**. Before a submission may be selected or published, the contributor must **expressly and verifiably accept the contribution license in the ticket**, including the potential future use of the **clue text** for AI model training or improvement if the required safeguards are met. Opening a ticket does not by itself constitute acceptance. Submissions are not required to play.

Ticket messages and attachments are processed through Discord and the Tickets Tools bot. Authorized moderation staff may review that material. The platform and ticket-bot provider may apply their own retention practices and terms; the actual settings and provider agreements must be checked. Users should avoid including other people's personal data in clues.

**No user-submitted puzzles are currently used for AI model training.** OpenAI is the intended provider for future editorial assistance; the integration has not been deployed. OpenAI API customer inputs are not used for model training by default unless the customer opts in.

If an external editorial provider is introduced, we intend to send **only clue text** after reviewing and removing detectable personal data. Discord IDs, usernames, avatars, answers, explanations and account data are not intended to be transmitted. A clue **cannot be presumed anonymous without prior review**.

Permission to exploit copyrighted material does not replace the legal basis required to process personal data included in it, or override GDPR rights. Before external training is enabled, the legal, contractual and technical compatibility, rights and safeguards will be checked and this Policy updated where needed.

## 5. Information visible to other players

Leaderboards and statistics may display Discord usernames. Conversations in the **public Discord workshop** are visible to people with access to that channel. Submissions intended for publication must go through a **private ticket**: access should be limited to the contributor, authorized moderators and necessary technical providers, depending on the actual permissions. Solutions for future daily puzzles should not be shared in the public workshop.

Published puzzles display the **username recorded when the work was contributed** by default, unless anonymity was requested and agreed before editorial acceptance. That attribution is a fixed snapshot and does not update automatically when a Discord username changes.

**Deleting an Activity account does not erase Discord tickets or messages.** Removing identifiers, deleting tickets and unlinking retained editorial copies requires a separate request to support, subject to technical capabilities and legal obligations. Content previously shared on third-party platforms may remain there.

Acceptance does not guarantee publication, and **scheduled publication dates are never disclosed in advance**. Replies may be communicated through the ticket while available; no in-Activity submission-status tracking or automatic notification is promised.

## 6. Service providers and recipients

- **Discord:** authentication, server membership, Activity distribution, **Premium subscription and payment management**, and ticket messages, attachments and public workshop discussions. Discord processes its own data under its terms.
- **Contabo:** the Fastify API and PostgreSQL database are deployed on a **Contabo VPS**, which also hosts Nginx and the game's static frontend files. Docker containers run on that VPS. The exact data-center location and appropriate Data Processing Agreement (DPA) must be checked and concluded as applicable; exclusive EU data residency is not assumed. Proposal tickets are handled separately through Discord.
- **Tickets Tools:** third-party bot used to create and manage proposal tickets within the Discord server; access to, and retention of, messages, attachments and metadata must be reviewed against its actual settings and applicable policy.
- **Cloudflare:** currently operates as the public proxy for `xzerep.es` and `criptico.xzerep.es`, with HTTPS at the edge and HTTPS to Nginx on Contabo. It may process IP addresses and connection metadata. Cloudflare Tunnel is not used in this deployment; other protections such as WAF will only be stated as active once verified.
- **Grafana:** planned technical monitoring tool; a centralized observability platform has not yet been verified as running for this deployment.
- **GitHub Pages:** publicly hosting these Terms and Privacy Policy. The service provider may process technical visitor information under its own terms.
- **OpenAI:** intended provider, **not yet integrated**, for future editorial assistance as described in section 4.

Technical access by collaborators and providers will be limited to what is needed for service delivery. We do not sell player data to advertisers.

## 7. International transfers

Discord, GitHub, Cloudflare or other providers may be involved in processing outside the European Economic Area. The Contabo data-center location and third-party processing must be verified; hosting PostgreSQL on a VPS does not guarantee that all processing stays in the European Economic Area, especially for submissions handled by Discord and ticket-bot providers.

Before enabling integrations involving international transfers, we will assess the actual contracting entities, relevant countries, subprocessors and required safeguards, including adequacy decisions or contractual clauses where applicable. You may request information about active service providers by contacting the controller.

## 8. Data retention and erasure

| Category                                            | Processing and retention                                                                                                                                                                                                                     |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Accounts, progress and gameplay                     | Data is retained while the account is needed to provide the service and is erased following authenticated account deletion, subject to legal duties. **Automatic erasure after 24 months of inactivity is planned but not yet implemented.** |
| Pending submissions                                 | **Planned editorial limit: 90 days from submission** if still pending. Automatic age-based cleanup is not yet deployed.                                                                                                                      |
| Rejected submissions                                | **Planned editorial limit: 30 days after rejection**. Automatic cleanup is not yet deployed.                                                                                                                                                 |
| Approved but unpublished submissions                | **Planned editorial limit: up to 12 months after acceptance**. Automatic cleanup is not yet deployed.                                                                                                                                        |
| Published contributions                             | Content may be retained during a valid license. In-game account deletion does not automatically remove Discord tickets or all editorial copies. |
| Editorial review notes                              | For published submissions, a **planned period of 30 days after publication**. Notes of rejected proposals follow the relevant rejection retention rule. Automatic rotation is not yet deployed.                                              |
| Submission replies and messages                     | May remain in tickets while they exist. There are no in-Activity proposal notices; Discord and the bot apply their own message-retention systems. |
| Premium entitlements and subscriptions | Discord-provided subscription access identifiers are retained as necessary to verify the entitlement, provide the service and meet applicable legal requirements. Discord administers billing under its own policies. |
| Support and privacy requests                        | Target retention of **up to 12 months after closure**, unless legal duties or pending disputes justify a different retention period.                                                                                                         |
| Technical logs, metrics and traces                  | **Target retention: up to 30 days on systems under our control**, not yet implemented and verified; local size-based Docker log rotation does not itself ensure this time limit; proxy, host system and any aggregator retention policies require separate configuration and verification.                                                                                                                                                 |
| Backups                                             | **Planned daily backups**, encrypted with a **maximum 30-day rotation** within the planned infrastructure. Deployment and restoration still need verification. Deleted data may remain temporarily in backups until their normal expiry.     |

The editorial targets above apply to copies controlled by Críptico Club and **do not guarantee automatic deletion of Discord messages or data held by Tickets Tools**. Ticket deletion requests must be handled separately through support. We do not claim that an undeployed automatic erasure process is already functioning. Planned retention periods will become operational commitments once implemented and verified.

## 9. Account deletion and data-subject rights

An authenticated **“Delete account and data”** option is available in **Profile → Settings**, subject to confirmation. It removes account records, gameplay history, XP, streaks, stored server membership and acceptance records. **Deleting a game profile does not automatically remove Discord tickets or messages or records retained by the ticket bot.** You may request their review or erasure through support. Editorial copies and attribution on previously published works may require additional handling.

Deleting a Críptico Club account **does not automatically cancel a Premium subscription purchased through Discord**: manage or cancel it separately in Discord. It also does not automatically remove Discord tickets or copies retained by third parties.

Depending on applicable law, you may request access, rectification, erasure, restriction, objection or portability and withdraw consent where personal-data processing actually relies on consent. Contact **zerep.a.p.s@gmail.com**. We may proportionately verify your identity before responding.

You may also submit a complaint to the [Spanish Data Protection Agency (AEPD)](https://www.aepd.es/).

## 10. Security, cookies and local technology

Access is verified through Discord and backend authorization controls. Activity session tokens are intended to remain temporary and in memory; we do not request your Discord password. The service uses technical request identifiers and checks to preserve integrity of gameplay and scoring.

We do not plan to use our own advertising pixels, marketing trackers or commercial profiling. Discord, Cloudflare, GitHub Pages and infrastructure security services may use cookies or other technical data under their own policies. Effective browser storage, logs and network calls will be audited before final launch.

## 11. Updates

We will publish a revised Policy if purposes, providers, data categories or retention periods change materially. Where legally required, affected users will receive further information or be asked for authorization before additional processing begins. The Spanish and English versions must remain materially equivalent.

**Contact:** **zerep.a.p.s@gmail.com**  
**Terms of Service:** [Read](../terms/)