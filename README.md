# Account Funding Tracker

## **Project Brief**

Background: OmniDex uses a series of accounts to execute oracle updates, liquidations, order executions and other functionality. These accounts require TLOS for gas, currently the accounts balances are monitored and updated manually. 

**Part 1.**   *Estimated time 2 - 3 hours.* 
Write a python script that tracks the balance of accounts. If any account balance falls below a certain threshold, send an SMS message with alert using [Twilio](https://www.twilio.com/docs/notify/quickstart/sms) (Use free trial for development).


|Account Name| Address | Min Amount (TLOS) |
|--|--|--|
| PositionKeeper | 0xFd60266002F4FAaBE8d8d9C66294EDe4810C6f34 |200| 
|OrderKeeper|0x948d447ef250E3468481E8622A475980F01015e1|200| 
|Liquidator|0x4Af5f783056C26231190DDC744D157e399488bbD|200| 
|PriceKeeper|0x4550AaB24fFc973dFf67882a6758cac43C5Cc605|500| 
|LendingPriceKeeper|0x27a9947FC9bE28b82ACa040433B25a1eb10C5Fe6|500| 
|DIAOracle|0x4b4c4a6e760fdea078efc6bea046946b639bddea|500| 




**Part 2.**  
Write a smart contract in solidity to periodically pay out TLOS from the contract to the addresses in Part 1 when they fall below their minimum account balance. When an account is paid, send an SMS message with the transaction hash, the update amount, and the contract's new TLOS balance. 


**Contract requirements:**

 - Contract must be [Ownable](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/access/Ownable.sol)
 - **Constructor**:   (Whitelisted addresses[], Emergency Withdraw address )
 - Deposit function (**onlyOwner**) 
 - Withdraw function: Withdraw TLOS to Emergency Withdraw address  (**onlyOwner**)  
 - Distribute Function: Distribute TLOS from the contract to whitelisted addresses. (**onlyOwner**)



**Code Practices**
1.  Consistent Indentation: Please use tabs throughout your codebase. This improves readability and makes your code more maintainable.
    
2.  Descriptive Variable and Function Names: Avoid single-letter variable names unless they have clear meanings within the context.
    
3.  Comments and Documentation: Include comments in your code to explain complex sections, provide context, and clarify your thought process.
    
4.  Error Handling: Implement appropriate error handling mechanisms. Use try-except blocks to catch and handle exceptions gracefully, providing informative error messages to help with debugging and troubleshooting.
    
5.  Modular Code: Break your code into smaller, reusable functions and classes. Modular code promotes reusability, readability, and easier maintenance. Each function or class should have a single responsibility and be relatively small.
