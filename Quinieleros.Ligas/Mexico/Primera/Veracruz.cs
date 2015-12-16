using System;

namespace Quinieleros.Ligas
{
	public class Veracruz : EquipoMexico
	{
		public Veracruz ()
		{
			this.Apodos = new System.Collections.Generic.List<string> (){ "El Tiburón","Los escualos" };
			this.Nombre = "Veracruz";
			this.Icon = "";
			this.id = "VERACRUZ";
		}
	}
}

