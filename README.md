# GPT-Projects

Welcome to GPT-Projects, a collection of small projects that showcase the use of OpenAI's GPT API in daily tasks.

## Projects

### Amazon Scrape

The Amazon Scrape project is a Python notebook that uses OpenAI's GPT API to extract product information from Amazon. Simply provide an initial query, the number of results, and your OpenAI API key, and the script will scrape the top search results and prioritize the products based on their relevance to the query and their properties. This can be a useful tool for anyone looking to quickly find the best products on Amazon for a given search query. You can see more about this project in <a href='https://orflow.wordpress.com/2023/04/16/using-gpt-api-to-find-and-compare-products-on-amazon/'>this blog post</a>.

To run the Amazon Scrape notebook, you can either use Google Colab, or run it locally.
To run it locally, you will need to have Python 3 installed on your computer, along with the following Python libraries:

- OpenAI
- Requests
- BeautifulSoup

Once you have the required libraries installed, simply download the `/amazon_scrape/amazon.ipynb` file, insert your API keys, and run it cell by cell.

### Telegram Bot

The Telegram bot project showcases a chatbot built using the GPT-4 API and Telegram Bot API. The chatbot can communicate with the GPT-4 model and generate responses to user messages. You can see more about this project in <a href='https://orflow.wordpress.com/2023/05/01/simple-telegram-chatbot-with-gpt-4/'>this blog post</a>.

To run it locally, you will need to have Python 3 installed on your computer, along with the following Python libraries:
- OpenAI
- pyTelegramBotAPI

Once you have the required libraries installed, simply download the `/telegram_bot/telegram_bot.py` file, insert your API keys, and run it. Once the chatbot is running, you can communicate with it through Telegram. Send a message to the bot, and it will generate a response using the GPT-4 model.

## Contributing

If you have any ideas for new projects or improvements to existing ones, we welcome contributions from the community. Please feel free to submit pull requests or open issues in the repository.

## License

GPT-Projects is licensed under the Apache License. See the LICENSE file for more information.
