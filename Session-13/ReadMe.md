# Mermaid Flowcharts

```mermaid
flowchart TD
  start_code([start])
  end_code([end])
  A[Get Name]
  B[Get Year]
  C[[Calculate Age]]
  D[/Display Age/]
  E{age > 18}
  F[/display you can vote/]
  G[/display we value your opinion, but no voting for you/]
    
  start_code --> A
  A --> B
  B --> C
  C --> D
  D --> E
  E --> |yes| F
  E --> |no| G

  F --> end_code
  G --> end_code

  
```