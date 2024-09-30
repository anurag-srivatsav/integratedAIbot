# integratedAIbot
 Interactive AI Profile Bot



Portfolio Bot is an interactive AI bot built with Streamlit that answers questions related to the user and provides information from external sources. This bot utilizes a custom knowledge base and Gemini API keys to deliver accurate and relevant responses.

![Portfolio Bot Screenshot](https://res.cloudinary.com/dvlgixtg8/image/upload/v1721070263/PortfolioBot.jpg)

## Features

- **Personal Information**: Answers questions about the user.
- **External Queries**: Provides information from external sources using the Gemini API.
- **Interactive Interface**: User-friendly and engaging interaction with the bot.
- **Knowledge Base**: Custom knowledge base to store and retrieve information.
- **API Integration**: Seamless integration with Gemini API for external data.

## Installation

To run the Portfolio Bot locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    https://github.com/anurag-srivatsav/PortfolioBot.git
    cd portfolio-bot
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**:
    Create a `.env` file in the root directory and add your Gemini API keys:
    ```plaintext
    GEMINI_API_KEY=your_gemini_api_key
    
    ```

4. **Run the Application**:
    ```bash
    streamlit run app.py
    ```

## Usage

After starting the application, a Streamlit server will run and provide a local URL (e.g., `http://localhost:8501`). Open this URL in your browser to interact with the Portfolio Bot. Ask questions related to the user or any other topic, and the bot will provide responses using the knowledge base and Gemini API.

## Project Structure

- `app.py`: Main application file to run the bot.
- `requirements.txt`: List of dependencies.
- `assets/`: Images and other assets.
- `knowledge_base/`: Custom knowledge base files.

## Example Interaction

![Example Interaction](https://res.cloudinary.com/dvlgixtg8/image/upload/v1721069452/BotScreenshot.jpg)

## Contributing

Contributions are welcome! If you have any ideas or improvements, please feel free to submit a pull request or open an issue.



## Contact

For any questions or suggestions, please contact [yourname@example.com](anuragsrivatsav4@gmail.com).
