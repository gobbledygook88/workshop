Backend development workshop
============================

Aim:

## 🟢  Objectives 

### 🎲 Playing your first game

Create a `POST /game` API which accepts the following JSON _request_

```javascript
{
  "playerPlayed": "paper"  // accepted values: rock, scissors, paper
}
```

The API should return the following JSON _response_

```javascript
{
  "gameId": "abc-defg-hijk"  // uuid
  "playerPlayed": "paper",
  "serverPlayed": "rock",
  "result": "you won!"       // possible values: "you won!" or "server won!"
}
```

You're free to choose any programming language you prefer!

What value the server responds with is completely up to you 😈

<details><summary>Things to consider</summary>

* TDD (compulsory _wink wink_)
* Try running the web server locally and use [`cURL`](https://everything.curl.dev/http/post) as an integration test
* Which [HTTP response codes](https://httpstatuses.coml) should we use?
* How can we validate the request payload to only allow the possible values?
* The request and response payloads use [camel-case](https://en.wikipedia.org/wiki/Camel_case), does that match the [naming convention](https://en.wikipedia.org/wiki/Naming_convention_(programming)#Language-specific_conventions) of your chosen programming language?
</details>

### 🔀 CI Pipelines

Setup various [Github Actions](https://github.com/features/actions) to run when code has been pushed to a branch

* Check code has been formatted
* Run all tests

<details><summary>Things to consider</summary>

* Be sure to configure your formatter via a configuration file and commit it to source control too
* What test runners are available for your language?
* Consider adding a [workflow status badge]](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge) to the README!
* Are there any other checks you'd like to automate?
</details>

### 🗃️  Storing results 

Now we want to introduce some storage to our application so that all played games are recorded for all eternity!

Our API generates random `gameId`s

<details><summary>Things to consider</summary>

</details>

### 🚜 Deployment

<details><summary>Things to consider</summary>

</details>

### 🔍 Querying results

<details><summary>Things to consider</summary>

</details>

### 👀 Viewing results

<details><summary>Things to consider</summary>

</details>

### ✏️  Draw an architecture diagram

White-boarding is an important skill. But not for interviews!

All parts of a tech stack are complicated with lots of layers. We need to be able to communicate how a system is made up by describing it with just the right level of detail.

Given all the components you've built so far, draw a diagram which demonstrates how an action from the frontend will propagate through the system.

<details><summary>Things to consider</summary>

* Start from the user's perspective and follow the actions through the whole system
* What are the key services an API request interacts with?
* How does the API response travel back to the user?
</details>

### 👪 Play against someone else!

Update your POST API to accept an extra parameter

```javascript
{
  "player": "rock",
  "serverURL": "https://some.server"
}
```

If a `serverURL` is given, your API should make a play on your behalf and return the results as before. You can expect the other API to accept the same JSON request as yours.

The results of any games should be stored.

<details><summary>Things to consider</summary>

* What useful fields would be useful to return in the API response?
* Are there any new columns to add to the database table?
</details>

### 👽 The future

Lots more exercises to come! Watch this space 😄

If you have any ideas, let me know! 🙇

#### 🌻 Ideas

* Scaling an API with docker via performance benchmarking
* Deploying the application on Kubernetes
* Going serverless
