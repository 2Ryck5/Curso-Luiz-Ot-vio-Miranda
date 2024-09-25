#Abstração
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'



class log:
    def _log(self,msg):
        raise NotImplementedError('implemente o método log')
    
    def log_error(self,msg):
        return self._log(f'Error:{msg}')
    
    def log_success(self,msg):
        return self._log(f'Success:{msg}')
    

class LogFileMixin(log):
    def _log(self,msg):
        msg_formatada = f"{msg} ({self.__class__.__name__})"
        print('Salvando no log:', msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')
        
class LogPrintMixin(log):
    def _log(self,msg):
        print(f"{msg} ({self.__class__.__name__})")
        
        
        
        
    
if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Erro no cadastro')
    lp.log_success('legal')
    lf = LogFileMixin()
    lf.log_error('Erro no cadastro')
    lf.log_success('legal')
