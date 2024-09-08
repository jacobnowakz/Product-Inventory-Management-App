Installation:
  1. Clone repo or download zip and extract
  2. Install Python and other dependencies via CMD or by running ..\Product-Inventory-Management-App-main\install_deps.bat as Administrator
     - winget install python
     - pip install typer
     - pip install -U pytest

Usage:
  1. Open CMD as administrator
  2. Navigate to ..\Product-Inventory-Management-App-main\Product-Inventory-Management-App-main
  3. Run "python main.py", the output should look like this: ![image](https://github.com/user-attachments/assets/a1572db8-61c8-4fd5-87da-dd793d6bbdda)

  4. To interact with the inventory via the CLI, run one of these commands:

       -"python main.py add-product [Product_ID] [Name] [Category] [Price] [Quantity]"                                                                                                        
       -"python main.py add-stock [Product_ID] [Quantity]"                                                                                                           
       -"python main.py display-product [Product_ID]"                                                                                                     
       -"python main.py generate-low-stock-report"                                                                                                     
       -"python main.py generate-report"                                                                                                     
       -"python main.py remove-product [Product_ID]"                                                                                                     
       -"python main.py remove-stock [Product_ID] [Quantity]"                                                                                                     
