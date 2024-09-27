# Complete YouTube Automation Pipeline

## Introduction

The **Complete YouTube Automation Pipeline** is an end-to-end automation solution designed to streamline the process of creating and uploading videos to a YouTube channel. By providing a link as input, the pipeline handles the entire content creation process: generating a script, creating an audio file, scraping relevant images, assembling the video, and automatically uploading the video to a YouTube channel. Additionally, a frontend interface is available that retrieves up-to-date information from the YouTube channel and displays recent posts and descriptions.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [FrontEnd Interface](#frontend-interface)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Features

- **Script Generation**: Automatically generates a script based on the provided link.
- **Audio File Creation**: Converts the generated script into an audio file using text-to-speech technology.
- **Web Scraping for Images**: Scrapes the web for images relevant to the content.
- **Video Assembly**: Combines the audio file and images into a complete video.
- **YouTube Upload**: Automatically uploads the generated video to a specified YouTube channel.
- **FrontEnd Dashboard**: Displays the most recent videos and posts from the YouTube channel, along with brief descriptions.

## Installation

### Backend

1. Clone the repository:

    ```bash
    git clone https://github.com/username/youtube-automation-pipeline.git
    cd youtube-automation-pipeline
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up API keys and credentials for YouTube, web scraping, and text-to-speech services. Place them in an `.env` file in the root directory.

### FrontEnd

1. Navigate to the frontend folder:

    ```bash
    cd frontend
    ```

2. Install frontend dependencies:

    ```bash
    npm install
    ```

3. Run the frontend application:

    ```bash
    npm start
    ```

## Usage

1. **Backend**:
    - To start the automation pipeline, run the following command, providing the input link:

    ```bash
    python run_pipeline.py --url <link_to_content>
    ```

    - The pipeline will automatically generate a script, create an audio file, scrape for images, assemble the video, and upload it to the YouTube channel.

2. **FrontEnd**:
    - After the frontend application is running, open the interface in your browser (usually available at `http://localhost:3000` by default).
    - The dashboard will display up-to-date information from the YouTube channel, including recent posts and brief descriptions.

## Dependencies

- **Backend**:
  - Python 3.x
  - Required libraries (see `requirements.txt`):
    - `youtube-upload-api`
    - `text-to-speech-sdk`
    - `beautifulsoup4`
    - `moviepy`
    - etc.

- **Frontend**:
  - Node.js
  - React.js
  - Required npm packages (see `package.json`):
    - `axios`
    - `react-router-dom`
    - etc.

## Configuration

- **YouTube API Key**: Required for uploading videos to your channel.
- **Text-to-Speech API Key**: Needed to convert the script to audio.
- **Web Scraping**: Ensure that the pipeline can access the necessary image sources for scraping.
- Place all API keys in an `.env` file with the following format:

    ```env
    YOUTUBE_API_KEY=your_youtube_api_key
    TTS_API_KEY=your_text_to_speech_api_key
    ```

## FrontEnd Interface

The frontend dashboard retrieves data directly from the associated YouTube channel and displays:

- **Recent Posts**: Lists the most recent videos uploaded to the channel.
- **Video Descriptions**: Provides brief descriptions of each video for easy review.
  
Users can easily navigate through recent content and access the latest videos uploaded by the automation pipeline.

## Troubleshooting

- **Video Upload Issues**: Ensure that the YouTube API key is correct and the credentials are valid.
- **Audio Generation Failure**: Verify that the text-to-speech API key is correctly configured.
- **Web Scraping Errors**: Ensure the content source link is accessible and that there are no blocking issues (e.g., CAPTCHA).

## Contributors

- Bamlak Deju Abera

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
