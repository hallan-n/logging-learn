## Introdução aos Logs  
Logs são registros de eventos importantes que acontecem em um sistema.  
Eles ajudam a monitorar o comportamento da aplicação e podem ser usados para debug e auditoria.  

### Exemplos de eventos que podem ser logados:  
- **Login/logout** de usuários.  
- **Execução de funções críticas.**  
- **Erros e falhas na aplicação.**  

---


## Níveis de log
Os logs podem ser categorizados em diferentes níveis de importância:

- DEBUG – Para informações detalhadas de depuração.
- INFO – Informações gerais do funcionamento da aplicação.
- WARNING – Algo inesperado, mas que não causa erro.
- ERROR – Ocorreu um erro que precisa ser corrigido.
- CRITICAL – Falha grave no sistema.

## Handlers (Saídas dos logs)
Os logs podem ser direcionados para diferentes destinos, como:

- Console (StreamHandler)
- Arquivos (FileHandler)
- E-mails (SMTPHandler)
- Requisições HTTP (HTTPHandler)