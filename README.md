Backend development workshop
============================

![Animal Crossing crafting screenshot](https://oyster.ignimgs.com/mediawiki/apis.ign.com/animal-crossing-new-horizons/c/c4/Screen_Shot_2020-02-03_at_2.48.55_PM.png?width=1280)

## 🎉 Aim

By completing a series of small exercises, we hope to build up our experience in backend development. We assume no knowledge, so we will be introducting and explaining various concepts along the way.

The exercises may dip into some DevOps and Infrastructure tasks. This is all in the hope of building out our overall engineering toolkit.

## 🏃 Exercises

Fork this repository and start working through the exercises in order 😄

This README may be updated in the future, so be sure to [merge from upstream into your fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/merging-an-upstream-repository-into-your-fork) regularly.

### 🎲 Playing your first game

We're going to be playing [rock, paper, scissors](https://en.wikipedia.org/wiki/Rock_paper_scissors) with a server. Any two-player game can be chosen, but try to keep it simple for your first attempt.

Create a `POST /game` API which accepts the following JSON request

```javascript
{
  "playerPlayed": "paper"  // accepted values: rock, scissors, paper
}
```

The API should return the following JSON response

```javascript
{
  "gameId": "abc-defg-hijk"            // uuid
  "playerPlayed": "paper",
  "serverPlayed": "rock",
  "result": "you won!",                // possible values: "you won!" or "server won!"
  "timestamp": "2021-12-01T10:10:00Z"  // date and time of when the game was played
}
```

You're free to choose any programming language you prefer!

What value the server responds with is completely up to you 😈

<details><summary>🚨 Things to consider</summary>

* TDD (compulsory 😉)
* Try running the web server locally and use [`cURL`](https://everything.curl.dev/http/post) as an integration test
* Which [HTTP response codes](https://httpstatuses.com) should we use?
* How can we validate the request payload to only allow the possible values?
* The request and response payloads use [camel-case](https://en.wikipedia.org/wiki/Camel_case), does that match the [naming convention](https://en.wikipedia.org/wiki/Naming_convention_(programming)#Language-specific_conventions) of your chosen programming language?
</details>

### 🔀 CI Pipelines

Setup various [Github Actions](https://github.com/features/actions) to run when code has been pushed to a branch

* Check code has been formatted
* Run all tests

<details><summary>🚨 Things to consider</summary>

* Be sure to configure your formatter via a configuration file and commit it to source control too
* What test runners are available for your language?
* Consider adding a [workflow status badge](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge) to the README!
* Are there any other checks you'd like to automate?
</details>

### 🗃️  Storing results

Now we want to introduce some storage to our application so that all played games are recorded for all eternity!

Our API generates random `gameId`s. Let's use that to reference past games in the future.

Choose a database which you think will be suitable, or you think will be fun to try!

How you run the database locally will depend on your operating system, but the next section might help.

<details><summary>🚨 Things to consider</summary>

* What data should be stored based on potential use cases?
* How should the data be stored?
* Is there any extra configuration to make querying easier?
</details>

### 🚀 Deployment

We'd like anyone to be able to clone our repository and easily run the application (API and database) with any configuration we choose to set.

To do this, we can make use of [docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/) to programmatically define all the resources we need to run our application.

This isn't the only way to build and deploy applications, can you think of any others? Would any be simpler and quicker to initially get working?

<details><summary>🚨 Things to consider</summary>

* Typos always happens. If there are any problems, look for error logs
* Is there anything we can add to CI to ensure our deployment configuration keeps working?
</details>

### 🔍 Querying results

Now that we have lots of data, we want to make use of it!

Create another API (`GET /game/<gameId>`) which returns a list of game results.

```javascript
{
  "games": [
    {
        "gameId": "abc-defg-hijk"
        "playerPlayed": "paper",
        "serverPlayed": "rock",
        "result": "you won!",
        "timestamp": "2021-12-01T10:10:00Z"
    },
    {
        "gameId": "fgh-asdu-ksdf"
        "playerPlayed": "scissors",
        "serverPlayed": "rock",
        "result": "server won!",
        "timestamp": "2021-12-11T11:11:00Z"
    }
  ]
}
```

<details><summary>🚨 Things to consider</summary>

* How should the game results be ordered?
* Can we reuse anything we have so far to ensure consistency?
* What should be returned if there are no games in the database?
* What should happen if `gameId` does not exist?
</details>

### 👀 Viewing results

Given your now infamous game server, people are curious as to the algorithm!

Those trade secrets aren't for public viewing, but you can release some charts to satisfy people's curiousity.

Create a simple page displaying a few charts. Here are some examples:

* Number of games played per person
* Win rate per the first move

<details><summary>🚨 Things to consider</summary>

* Think about how to expose that information via the API. Would it change if you had millions of players?
* If you're using [postgres](https://www.postgresql.org/), try out [psql](https://www.postgresql.org/docs/9.3/app-psql.html) or [pgcli](https://www.pgcli.com/) to test out SQL queries
</details>

### ✏️  Draw an architecture diagram

White-boarding is an important skill. But not for interviews!

All parts of a tech stack are complicated with lots of layers. We need to be able to communicate how a system is made up by describing it with just the right level of detail.

Given all the components you've built so far, draw a diagram which demonstrates how an action from the frontend will propagate through the system.

<details><summary>🚨 Things to consider</summary>

* Start from the user's perspective and follow the actions through the whole system
* What are the key services an API request interacts with?
* How does the API response travel back to the user?
</details>

### 👪 Play against someone else!

Let's dive deeper into databases and data modelling.

We want our application to support multiple players. Players should be allowed to asynchronously submit their moves, and the server will respond with the result as before.

<details><summary>🚨 Things to consider</summary>

* We currently have a `game` schema. Are their any additional schemas which would be useful to add?
* Are there any relationships between the schemas?
* Are the changes backwards compatible, or will existing functionality break?
* Will we need new APIs to support multi-player games, or can existing APIs support them? What is the maintenance cost of the additional features?
</details>

### 👽 The future

Lots more exercises to come! Watch this space 😄

If you have any ideas, let me know! 🙇

#### 🌻 Ideas

* Pagination of game results API; [HAL](https://stateless.group/hal_specification.html)
* Scaling an API with docker via performance benchmarking
* Deploying the application on a cloud provider with infrastructure as code
* Going serverless (as opposed to using docker)
* Adding authentication
* Configuring and securing the network stack
* Websockets for 2-player notifications
* REST vs GraphQL
