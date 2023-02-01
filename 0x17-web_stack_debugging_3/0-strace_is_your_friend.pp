# fixex apache 500 error
exec { 'fix-php-typo':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin';
}
