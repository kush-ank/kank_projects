/*insert data into an address table*/

var1 ADDRESS.ADR_TYP_DESC%type := 'home';
var2 ADDRESS.DATA_SRC%type := 'advisors';

BEGIN
     BEGIN
	      -- INSERT DATA INTO THE ADDRESS TABLE
		  INSERT INTO ADDRESS
		  (ADDR_ID,
		  ADDR_ST_DT,
		  ADDR_LINE_1,
		  ADDR_LINE_2,
		  ADDR_LINE_3,
		  CITY_NM,
		  STATE_NM,
		  POSTAL_CD,
		  CTRY_NM,
		  ADDR_TYP,
		  ADDR_DATA_SRC)
		  VALUES 
		  (i_addr_id,
		  SYSDATE,
		  i_addr_lin_1,
		  i_addr_lin_2,
		  NULL,
		  i_city_name,
		  i_state_nm,
		  i_postal_cd,
		  i_ctry_nm,
		  var1,
		  var2);
		  
		  COMMIT;
		  
	 EXCEPTION WHEN DUP_VAL_ON_INDEX THEN NULL; -- THIS IS FUNCTION NOT CREATED YET IN THE SP
	           WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE('Address error message='||SQLERRM);
			   
	 RAISE NORECOVER;
	 END;
END;