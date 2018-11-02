from proxy1.proxypool.api import app
from proxy1.proxypool.schedule import Schedule

def main():

    s = Schedule()
    s.run()
    app.run("0.0.0.0",5000)


if __name__ == '__main__':
    main()

