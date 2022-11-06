<p align="center">
  <a href="https://gofiber.io">
    <img alt="logo" height="150" src="https://i.ibb.co/pQDGTfY/Monitor.png">
  </a>
  <br>
  <a href="https://gocover.io/github.com/gofiber/fiber">
    <img src="https://img.shields.io/badge/%F0%9F%94%8E%20gocover-97.8%25-75C46B.svg?style=flat-square">
  </a>
  <a href="https://github.com/gofiber/fiber/actions?query=workflow%3ASecurity">
    <img src="https://img.shields.io/github/workflow/status/gofiber/fiber/Security?label=%F0%9F%94%91%20gosec&style=flat-square&color=75C46B">
  </a>
  <a href="https://github.com/gofiber/fiber/actions?query=workflow%3ATest">
    <img src="https://img.shields.io/github/workflow/status/gofiber/fiber/Test?label=%F0%9F%A7%AA%20tests&style=flat-square&color=75C46B">
  </a>
    <a href="https://docs.gofiber.io">
    <img src="https://img.shields.io/badge/%F0%9F%92%A1%20fiber-docs-00ACD7.svg?style=flat-square">
  </a>
  <a href="https://gofiber.io/discord">
    <img src="https://img.shields.io/discord/704680098577514527?style=flat-square&label=%F0%9F%92%AC%20discord&color=00ACD7">
  </a>
  
</p>
<p align="center">
  <b>Curve Monitor</b> is a project inspired by <b>hal.xyz</b> built with Python designed to allow users to receive <b>alerts</b> regarding <b>Curve pool performance</b> to their favorite messaging platforms like <b>Slack</b> and <b>Telegram</b>.
</p>
<p align="center">
  <b>Current Supported Messaging Platforms:</b> Slack, Telegram
</p>

## ⚙️ Installation
___

Make sure you have Python installed ([download](https://www.python.org/downloads/)). Version `3.9` or higher is required.

Initialize your project by cloning the repository:

```shell
git clone https://github.com/PathX-Projects/Curve-Monitor.git

cd Curve-Monitor/
```

Install/upgrade package requirements:

```shell
pip install --upgrade -r requirements.txt
```

## ⚡️ Quickstart
___

Launch the software using the -m flag to run the module from the **\_\_main\_\_.py** script.
```bash
python3 -m curve_monitor
```
(Optional - Requires Mac or Linux OS) Run the UNIX CLI tool to manage alerts:
```bash
bash unix_cli.sh
```



## 👀 Examples
___

Listed below are some of the common examples. If you want to see more code examples , please visit our [Recipes repository](https://github.com/gofiber/recipes) or visit our hosted [API documentation](https://docs.gofiber.io).

#### 📖 [**Basic Routing**](https://docs.gofiber.io/#basic-routing)

```go
func main() {
    app := fiber.New()

    // GET /api/register
    app.Get("/api/*", func(c *fiber.Ctx) error {
        msg := fmt.Sprintf("✋ %s", c.Params("*"))
        return c.SendString(msg) // => ✋ register
    })

    // GET /flights/LAX-SFO
    app.Get("/flights/:from-:to", func(c *fiber.Ctx) error {
        msg := fmt.Sprintf("💸 From: %s, To: %s", c.Params("from"), c.Params("to"))
        return c.SendString(msg) // => 💸 From: LAX, To: SFO
    })

    // GET /dictionary.txt
    app.Get("/:file.:ext", func(c *fiber.Ctx) error {
        msg := fmt.Sprintf("📃 %s.%s", c.Params("file"), c.Params("ext"))
        return c.SendString(msg) // => 📃 dictionary.txt
    })

    // GET /john/75
    app.Get("/:name/:age/:gender?", func(c *fiber.Ctx) error {
        msg := fmt.Sprintf("👴 %s is %s years old", c.Params("name"), c.Params("age"))
        return c.SendString(msg) // => 👴 john is 75 years old
    })

    // GET /john
    app.Get("/:name", func(c *fiber.Ctx) error {
        msg := fmt.Sprintf("Hello, %s 👋!", c.Params("name"))
        return c.SendString(msg) // => Hello john 👋!
    })

    log.Fatal(app.Listen(":3000"))
}

```