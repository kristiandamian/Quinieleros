using System;

namespace Quinieleros.Ligas
{
	public class America : EquipoMexico
	{
		public America ()
		{
			this.Apodos = new System.Collections.Generic.List<string> (){ "Los Azulcremas", "El Ame", "Los millonetas", "Las águilas" };
			this.Nombre = "América";
			this.Icon = "";
			this.id = "AMERICA";
		}
	}
}

