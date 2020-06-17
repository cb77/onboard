from click.testing import CliRunner
from helloclick import hello


#search(path, ftype):
    
def test_hello():
  runner = CliRunner()
  result = runner.invoke(hello)
  assert result.exit_code == 0
  