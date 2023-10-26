Subfork Python API
==================

This package provides the Subfork Python API and command line interface.

Use the Python API for deploying sites and processing tasks using workers.


Installation
------------

The easiest way to install:

    $ pip install subfork


Definitions
-----------

Terminology used throughout:

- Datatypes are collections of related data records.
- Pages are template files that contain HTML content.
- Queues are named FIFO lists of Tasks.
- Tasks are a set of data that get processed Workers.
- Static files are images, css and javascript files.
- Workers process Tasks by passing data to a pre-defined Python function.


Configuration
-------------

To use environment variables, do the following:

    $ export SUBFORK_ACCESS_KEY=XXXXXX
    $ export SUBFORK_SECRET_KEY=XXXXXX

To use a shared config file, copy the `example_subfork.yaml` file to `subfork.yaml`
at the root of your project and make required updates:

    $ cp example_subfork.yaml subfork.yaml
    $ nano subfork.yaml

Or set `$SUBFORK_CONFIG_FILE` to the path to `subfork.yaml`:

    $ export SUBFORK_CONFIG_FILE=/path/to/subfork.yaml


Basic Commands
--------------

To deploy a site:

    $ subfork deploy [template.yaml] -c <comment> [--release]

To test the site using the dev server:

    $ subfork run [template.yaml]

To process tasks:

    $ subfork worker [options]


Site Templates
--------------

The `template.yaml` file contains the site template and static file information,
for example:

    domain: myapp.fork.io
    pages:
      index:
        route: /
        file: index.html
      item:
        route: /item/<itemid>
        file: item.html


Data
----

Data is stored as `Datatype` records.

Insert some data:

    >>> sf = subfork.get_client()
    >>> sf.get_data(datatype).insert(record)

Find some data matching a list of search params:

    >>> results = sf.get_data(datatype).find(params)

where `params` is a list of [key, op, value] lists, for example:

    >>> events = sf.get_data("event").find([["location", "=", "LA"]])


Workers
-------

Workers process tasks created either via API clients or users.
By default, running the `subfork worker` command will pull tasks from a
specified queue and process them.

    $ subfork worker [--queue <queue> --func <pkg.mod.func>]

For example:

    $ subfork worker --queue test --func subfork.worker.test

Workers can also be defined in the `subfork.yaml` file:

    WORKER:
      name:
        queue: test
        function: subfork.worker.test

To create tasks, POST key/value data to a queue. The response will include
the task id:

    >>> sf = subfork.get_client()
    >>> task = sf.get_queue("test").create_task({"t": 3})

To get task results:

    >>> task = sf.get_queue("test").get_task(taskid)
    >>> task.data()

Running a worker as a service:

See the `bin/worker` and `services/worker.service` files for an example of how
to set up a systemd worker service. 

Update the ExecStart and Environment settings with the correct values, and copy
the service file to /etc/systemd/system/ and start the service.

    $ sudo cp services/worker.service /etc/systemd/system/
    $ sudo systemctl daemon-reload
    $ sudo systemctl start worker
    $ sudo systemctl enable worker

Checking worker logs:

    $ sudo journalctl -u worker -f
