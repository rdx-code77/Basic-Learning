while($row = $result->fetch_assoc())
{
?>
<tr>
<td ><?php echo $row["SNo"]; ?></td>
<td style="text-align:left;" ><?php echo $row["email"]; ?></td>
<td ><?php echo $row["action"];?></td>
<td ><?php echo $row["date_time"];?></td>
</tr>

<?php
 }