
  ** Configuration validation for LPA**
    
    1. Test for workflowconfig.json schema validation - This test case does a schema validation for the workflowconfig.json in terms of optional and mandatory fields.
       Also verify if the datatype for boolean, integer and alphanumeric are proper
        
    2. Test for transformconfig.json schema validation - This test case does a schema validation for the transformconfig.json in terms of optional and mandatory fields.
       Also verify if the datatype for boolean, integer and alphanumeric are proper
       
    3. Test for Service Definition and Workflow dependency - This test case verifies if all the entities present in the service definition are also defined in the workflowconfig.json.
       We exclude outbound entities while executing this as the outbound entities mentioned in service defnition file are not mentioned in the workflowconfig.json
       
    4. Test for workflow and transformConfig dependency - This test case verifies if all the sub-entities mentioned in the workflowconfig.json are also present in the transformconfig.json.
    
    5. Test for incremental date when NEXT_DAY present in the workflowConfig - This test case verifies if the datePolicy has been defined as "NEXT_DAY" in the workflowconfig.json then
       the sub-entity also has incrementalDate configured in the file for that specific sub-entity
       
    6. Test for daily and historical present in the transformConfig for every entity - This verifies if the daily and historical configuration is present for each sub-entity in the transformconfig.json
    
    7. Verify if a path is given for the 'Delete' action for an entity if force delete is enabled - This verifies if a path is given for forced delete for each sub-entity in transformconfig.json 
    if the forced delete flag was enabled in the workflowconfig.json
    
    8. Validate message versions in transform config - This verifies if the message version in the transformconfig.json for each sub-entity are as per the versions provided in the service definition
    
    9. Validate if all entities in transform config support json - This verifies if all the sub-entities in transform config support json
    
    10. Validate the sequence of entitiies in workflow - This verifies if the sequence of all the sub-entities has been properly mentioned in an ordered manner in the workflowconfig.json
