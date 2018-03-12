# ai_api

A simple project for my master's university programming course. It sets up a Restful API using Flask, allow the user to train and predict using two simple AI models through requests and saves them on a SQLite3 usign SQLAlchemy.

## Getting Started

Simply clone the repository into your machine. It's that simple!

Just a fair warning: This program uses Theano, a machine-learning focused package that will be discontinued soon. I have plans to update this to TensorFlow, but I don't know when.

### Installing

First things first, you need to run the requirements.txt on your pip.

```
pip install -r requirements.txt
```

After that, the learn-utils package will be installed in your environment. To launch the API, simply run the following command on this project root.

```
flask-manager run
```

You can add the --dev option to this command to run it in development mode. Development mode allows for changes in the code without having to stop running the API and allows the full error message to appear. Great for... development.

## Running the tests

The learn-utils also has a function for running tests. Just run the following command.

```
flask-manager test --path {path}
```

At {path} you just need to put the path to the test file or folder.

## Built With

* [Flask](http://flask.pocoo.org/) - The API framework used
* [SQLAlchemy](https://www.sqlalchemy.org/) - Database management
* [Theano](http://deeplearning.net/software/theano/) - Toolkit for Machine-Learning code

## Authors

* **Gustavo Krieger** - *Initial work* - [GMKrieger](https://github.com/GMKrieger)

## License

This project is licensed under the MIT License

## Acknowledgments

* Thanks to my colleagues for helping me with the code. You know who you are =)


