# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sdk',
 'sdk.config',
 'sdk.decorators',
 'sdk.prompts',
 'sdk.tracing',
 'sdk.utils']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.6,<0.5.0',
 'deprecated>=1.2.14,<2.0.0',
 'jinja2>=3.1.2,<4.0.0',
 'opentelemetry-api>=1.20.0,<2.0.0',
 'opentelemetry-exporter-otlp-proto-grpc>=1.20.0,<2.0.0',
 'opentelemetry-exporter-otlp-proto-http>=1.20.0,<2.0.0',
 'opentelemetry-instrumentation-anthropic>=0.0.10,<0.0.11',
 'opentelemetry-instrumentation-chromadb==0.0.6',
 'opentelemetry-instrumentation-cohere>=0.0.6,<0.0.7',
 'opentelemetry-instrumentation-haystack>=0.0.8,<0.0.9',
 'opentelemetry-instrumentation-langchain==0.0.7',
 'opentelemetry-instrumentation-openai>=0.0.14,<0.0.15',
 'opentelemetry-instrumentation-pinecone>=0.0.10,<0.0.11',
 'opentelemetry-instrumentation-pymysql>=0.41b0,<0.42',
 'opentelemetry-instrumentation-requests>=0.41b0,<0.42',
 'opentelemetry-instrumentation-transformers==0.0.4',
 'opentelemetry-instrumentation-urllib3>=0.41b0,<0.42',
 'opentelemetry-sdk>=1.20.0,<2.0.0',
 'opentelemetry-semantic-conventions-ai>=0.0.7,<0.0.8',
 'pydantic>=1.10.12,<2.0.0',
 'tenacity>=8.2.3,<9.0.0']

setup_kwargs = {
    'name': 'traceloop-sdk',
    'version': '0.0.66',
    'description': 'Traceloop Software Development Kit (SDK) for Python',
    'long_description': '# traceloop-sdk\n\nTraceloop’s Python SDK allows you to easily start monitoring and debugging your LLM execution. Tracing is done in a non-intrusive way, built on top of OpenTelemetry. You can choose to export the traces to Traceloop, or to your existing observability stack.\n\n```python\nTraceloop.init(app_name="joke_generation_service")\n\n@workflow(name="joke_creation")\ndef create_joke():\n    completion = openai.ChatCompletion.create(\n        model="gpt-3.5-turbo",\n        messages=[{"role": "user", "content": "Tell me a joke about opentelemetry"}],\n    )\n\n    return completion.choices[0].message.content\n```\n',
    'author': 'Gal Kleinman',
    'author_email': 'gal@traceloop.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/traceloop/openllmetry',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4',
}


setup(**setup_kwargs)
